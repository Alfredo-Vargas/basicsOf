- The configuration files are stored in `$HOME/.aws/`
- Structure of the AWS commands:
```
aws <command> <subcommand> [options and parameters]
```
- Configure specific aws cli profiles:
```console
aws configure --profile <profile-name>
```

- Check the help or service specific help
```console
aws help
aws <service-name> <help>
```

- If the current profile has the right permissions, one can list the iam users:
```console
aws iam list-users
```
