provider "google" {
  credentials = "${file("core-catalyst-283702-30950e2a8fd2.json")}"
  project = "core-catalyst-283702"
  region = "us-central1"
}
