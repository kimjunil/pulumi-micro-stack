"""A Kubernetes Python Pulumi program"""

import pulumi
from pulumi_kubernetes.apps.v1 import Deployment, DeploymentSpecArgs
from pulumi_kubernetes.meta.v1 import LabelSelectorArgs, ObjectMetaArgs
from pulumi_kubernetes.core.v1 import ContainerArgs, PodSpecArgs, PodTemplateSpecArgs
import pulumi_kubernetes as k8s

config = pulumi.Config()
stack = pulumi.get_stack()

kubeconfig = config.require("kubeConfig")
# kubeconfig = "~/.kube/config"

pulumi.export("kubeConfig", kubeconfig)
