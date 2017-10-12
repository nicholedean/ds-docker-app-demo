## Deployment to AWS Elastic Beanstalk
**The Basic Commands**<br>
- eb init
- eb create
- eb status
- eb events
- eb logs
- eb open
- eb deploy
- eb config
- eb terminate

The general flow of procedures look as follow
```zsh
eb init
aws elasticbeanstalk describe-environments
eb create | eb deploy
```

For more details, refer to the official documentation at [here](http://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3.html)

## Notice
- The `src` can be renamed to whatever application name you feel like having
- Available Docker platform version.
    1) Docker 17.03.2-ce
    2) Docker 17.03.1-ce
    3) Docker 1.12.6
    4) Docker 1.11.2
    5) Docker 1.9.1
    6) Docker 1.7.1
    7) Docker 1.6.2
- Saved configuration for AWS Elasticbeanstalk can be edit and update