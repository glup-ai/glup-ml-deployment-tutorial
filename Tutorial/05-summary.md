# Machine Learning API Deployment Tutorial | Summary

This tutorial demonstrated two separate methods of how to deploy an ML inference application as a RESTful API - implementing a serverless function app and a hosted app service. Following either of the two should result in an applied model ready to be used by clients. The APIs can be employed by interactive web and mobile applications.

[https://cat.glup.ai](https://cat.glup.ai) presents an example of a static web application employing the tutorial example. [Click here](https://github.com/glup-ai/hipsterize-cat-frontend) for the frontend code repo.

## Machine learning project lifecycle

The API deployment procedure plays an essential role in the [machine learning project lifecycle](https://landing.ai/wp-content/uploads/2021/06/graphiclifecycle.png). The tutorial depicts the ML application evolution process - from a running cell on a laptop Jupyter Notebook, to a consumable API - a contributing factor in closing the [ML production gap](https://www.oreilly.com/radar/machine-learning-and-the-production-gap/).

## Limitations

Applications such as these **should not** be used in production-like systems with the current configurations. They are prone to **cold starts**, resulting in potentially substantial delays with the first requests after idle periods. The current arrangements involves initiation of the Python environment and all its dependencies, requiring a function/instance warm up. The subsequent requests will proceed in a more performant manner.

There are different ways to undertake [the cold start problem](https://azure.microsoft.com/en-us/blog/understanding-serverless-cold-start/). The easiest would be to upgrade to a more suitable hosting plan (:money_with_wings:) and also possibly enable the [Always on](https://docs.microsoft.com/en-us/azure/azure-functions/dedicated-plan#always-on) setting.

## Next steps

Visit [https://glup.ai](https://glup.ai) (in :norway:) to learn more about the ML project lifecycle and discover more AI projects.

![cat_02](images/cat_02.JPG)
