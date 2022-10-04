"""A Kubernetes Python Pulumi program"""

import pulumi
from pulumi_kubernetes.apps.v1 import Deployment, DeploymentSpecArgs
from pulumi_kubernetes.meta.v1 import LabelSelectorArgs, ObjectMetaArgs
from pulumi_kubernetes.core.v1 import ContainerArgs, PodSpecArgs, PodTemplateSpecArgs
from pulumi_kubernetes import Provider

env = pulumi.get_stack()

infra = pulumi.StackReference(f"kimjunil/infrastructure/{env}")
k8s = Provider("k8s", kubeconfig=infra.get_output("kubeConfig"), context="minikube")

flyte = pulumi.StackReference(f"kimjunil/flyte/{env}")

app_labels = { "app": "jupyterhub" }

deployment = Deployment(
    "jupyterhub",
    spec=DeploymentSpecArgs(
        selector=LabelSelectorArgs(match_labels=app_labels),
        replicas=1,
        template=PodTemplateSpecArgs(
            metadata=ObjectMetaArgs(labels=app_labels),
            spec=PodSpecArgs(containers=[ContainerArgs(name="jupyterhub", image="nginx")])
        ),
    ),
    opts=pulumi.ResourceOptions(provider=k8s))

pulumi.export("name", deployment.metadata["name"])
