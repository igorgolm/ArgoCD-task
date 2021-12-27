# Technical task for Igor Golm

The goals for this task are the following:

1. Set up a Github actions workflow in the https://github.com/verifa/igor-task Github repository which builds a new 
Docker Image and pushes it to [GCP Artifact registry](https://cloud.google.com/artifact-registry/docs) *europe-north1-docker.pkg.dev/lauri-container-fundamentals/fleuri/testapp* .

2. Fill in the kubernetes manifests for a deployment and service in the [kubernetes folder](kubernetes) for running the 
   testapp on kubernetes.   

3. Add instructions / a script / other automation for setting up a local kubernetes environment. Use minikube, kind or
similar.
   
4. Deploy testapp and ArgoCD on the local k8s and have ArgoCD update the deployment when a new change is committed. Test
the setup by committing an arbitrary code change to the testapp (for example, you could fix the timezone for get_time() function).
   
5. Demo your work to us when you are done!

6. Have fun! Don't be afraid to ask for help or clarifications, especially if something doesn't work as I planned.

#Authenticating with GCP Artifact Repository

To use the provided registry and the image within it ``` europe-north1-docker.pkg.dev/lauri-container-fundamentals/fleuri/testapp ```,
the user has to authenticate to it using the already created Service Account's (*artifact-repo-sa@lauri-container-fundamentals.iam.gserviceaccount.com*)
keyfile in the repo. Authenticate by running

    cat artifact-repo-sa-key64.json | docker login -u _json_key_base64 --password-stdin https://europe-north1-docker.pkg.dev
or

    cat artifact-repo-sa-key.json | docker login -u _json_key --password-stdin https://europe-north1-docker.pkg.dev

The Service Account has read and write permissions to the repo. If for some reason after successfully logging in you get
an error message like

    Error response from daemon: Head "https://europe-north1-docker.pkg.dev/v2/lauri-container-fundamentals/fleuri/testapp/manifests/latest": denied: Permission "artifactregistry.repositories.downloadArtifacts" denied on resource "projects/lauri-container-fundamentals/locations/europe-north1/repositories/fleuri" (or it may not exist)

try clearing your docker config by running ``` rm $HOME/.docker/config.json ```. 

#Notes about testapp

Testapp is a simple webapp conjured up with flask. The environment is setup with [direnv](https://direnv.net/) and it has
python3 and pip along with the dependencies installed. If you wish to set your own dev environment, you can install the
dependencies with ```pip install -r requirements.txt```.

To run the application locally, you can either run ```flask run``` with optional flags or build and run the docker container.

