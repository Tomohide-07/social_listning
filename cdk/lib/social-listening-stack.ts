import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as apprunner from 'aws-cdk-lib/aws-apprunner';
import * as ecr_assets from 'aws-cdk-lib/aws-ecr-assets';
import * as path from 'path'; 

export class SocialListeningStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const image = new ecr_assets.DockerImageAsset(this, 'AppImage', {
      directory: path.join(__dirname, '../../docker-app'),
    });

    new apprunner.CfnService(this, 'AppRunnerService', {
      serviceName: 'social-listening',
      sourceConfiguration: {
        authenticationConfiguration: {},
        imageRepository: {
          imageIdentifier: image.imageUri,
          imageRepositoryType: 'ECR',
          imageConfiguration: { port: '8501' }
        }
      }
    });
  }
}