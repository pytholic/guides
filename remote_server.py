We will use **Secure Shell SSH** to access the server and run commands.

# Server details

```
Host name: zeno
Host ip: 10.160.51.36
Username: pytholic
```

# Connecting to the server

Use `ssh` command with the address.

```
ssh 10.160.51.36 or ssh <username>@<address>
```

```
pytholic@pytholic-pc:~$ ssh 10.160.51.36
pytholic@10.160.51.36's password: 
Welcome to Ubuntu 22.04 LTS (GNU/Linux 5.15.0-41-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

64 updates can be applied immediately.
16 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable

Last login: Tue Aug  2 11:23:59 2022 from 10.160.51.34
```

# Exiting connection

Use `logout` command.

```
pytholic@zeno:~$ logout
Connection to 10.160.51.36 closed.
```

# Saving password

Use `ssh-keygen`. Reference [link](https://www.notion.so/Remote-Server-3ba3462c2e554194a2a8e62a6719817b).

```
ssh-keygen

Press ENTER for all the prompts, leave them empty.

ssh-copy-id -i ~/.ssh/id_rsa.pub pytholic@<server address/ip>

Enter password
```

Now try connecting and it should work without password.

# Creating config file

Better way is to store all the settings inside your `.ssh/config` file.

```
nano ~/.ssh/config
```

Add the following lines and save.

```
Host zeno
HostName 10.160.51.36
User pytholic
ForwardAgent yes
```

Then simply use `ssh zeno` to connect.

Reference [link](https://acarril.github.io/posts/ssh-sripts-st3).

# Checking ssh extension for VSCode

Installed **Remote-SSH** extension by Microsoft.

Then press `F1` and run the command `Remote-SSH: Connect to Host…`

Then use **File → Open Folder** to open any folder.

# File Transfer

Local to Remote

```
scp file.txt remote_username@10.10.0.2:/remote/directory
```

Remote to Local

```
scp remote_username@10.10.0.2:/remote/file.txt /local/directory
```
