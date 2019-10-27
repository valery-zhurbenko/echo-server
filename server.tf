resource "kubernetes_deployment" "server" {
  metadata {
    name = "server"
    labels = {
      App = "server"
    }
  }

  spec {
    replicas = 1
    selector {
      match_labels = {
        App = "server"
      }
    }
    template {
      metadata {
        labels = {
          App = "server"
        }
      }
      spec {
        container {
          image = "valery/echo-server-python:0.1"
          name  = "server"
          tty = true

          port {
            container_port = 5432
          }

          resources {
            limits {
              cpu    = "0.5"
              memory = "512Mi"
            }
            requests {
              cpu    = "250m"
              memory = "250Mi"
            }
          }
        }
      }
    }
  }
}

resource "kubernetes_service" "server" {
  metadata {
    name = "server"
  }
  spec {
    selector = {
      App = kubernetes_deployment.server.spec.0.template.0.metadata[0].labels.App
    }
    port {
      port        = 8432
      target_port = 5432
      node_port   = 32555
    }

    external_ips = [ "192.168.99.100", "10.0.2.15" ]

    type = "LoadBalancer"
  }
}