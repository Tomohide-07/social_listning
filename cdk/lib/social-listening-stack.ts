import * as cdk from 'aws-cdk-lib';
import { Construct } from 'constructs';
import * as apprunner from 'aws-cdk-lib/aws-apprunner';
import * as ecr_assets from 'aws-cdk-lib/aws-ecr-assets';

export class SocialListeningStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Docker イメージをビルドして ECR アセットに登録
    const image = new ecr_assets.DockerImageAsset(this, 'AppImage', {
      directory: '../',  // ルートの Dockerfile を参照
    });

    // App Runner サービスを作成
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