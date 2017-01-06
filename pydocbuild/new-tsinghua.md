Android 镜像使用帮助 {#android-}
--------------------

**注意: 本镜像是 AOSP 镜像，Android SDK因版权原因，我们不能提供镜像服务。**

参考 Google 教程 <https://source.android.com/source/downloading.html>， 将 `https://android.googlesource.com/` 全部使用 `https://aosp.tuna.tsinghua.edu.cn/` 代替即可。

由于使用 HTTPS 协议更安全，并且更便于我们灵活处理，所以强烈推荐使用 HTTPS 协议同步 AOSP 镜像。

**由于 AOSP 镜像造成CPU/内存负载过重，我们限制了并发数量，请尽量错峰(凌晨)同步。**

-   **2016-06-24 : 关闭 git:// 协议，仅支持 HTTPS**
-   **2016-04-03 : 删除每月初始化包中的冗余内容，使用方法更新**
-   **2015-12-21 : 增加每月初始化包，少量修正文档错误**
-   **2015-10-13 : 修复上游替换文档错误**
-   **2015-10-13 : 修复次级镜像文档错误**
-   **2015-10-09 : 恢复 git://aosp.tuna.tsinghua.edu.cn/aosp/ 访问**
-   **2015-10-08 : 镜像地址更新为 https://aosp.tuna.tsinghua.edu.cn/ (结尾没有/android)**

### 过程摘录 {#section}

(参考 <https://lug.ustc.edu.cn/wiki/mirrors/help/aosp> 编写)

下载 repo 工具:

    mkdir ~/bin
    PATH=~/bin:$PATH
    curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
    chmod a+x ~/bin/repo

或者使用tuna的[git-repo镜像](https://mirrors.tuna.tsinghua.edu.cn/help/git-repo/)

#### 使用每月更新的初始化包 {#section-1}

由于首次同步需要下载 24GB 数据，过程中任何网络故障都可能造成同步失败，我们强烈建议您使用初始化包进行初始化。

下载 <https://mirrors.tuna.tsinghua.edu.cn/aosp-monthly/aosp-latest.tar>，下载完成后记得根据 checksum.txt 的内容校验一下。

由于所有代码都是从隐藏的 `.repo` 目录中 checkout 出来的，所以我们只保留了 `.repo` 目录，下载后解压 再 `repo sync` 一遍即可得到完整的目录。

使用方法如下:

    wget https://mirrors.tuna.tsinghua.edu.cn/aosp-monthly/aosp-latest.tar # 下载初始化包
    tar xf aosp-latest.tar
    cd AOSP   # 解压得到的 AOSP 工程目录
    # 这时 ls 的话什么也看不到，因为只有一个隐藏的 .repo 目录
    repo sync # 正常同步一遍即可得到完整目录
    # 或 repo sync -l 仅checkout代码

此后，每次只需运行 `repo sync` 即可保持同步。 **我们强烈建议您保持每天同步，并尽量选择凌晨等低峰时间**

#### 传统初始化方法 {#section-2}

建立工作目录:

    mkdir WORKING_DIRECTORY
    cd WORKING_DIRECTORY

初始化仓库:

    repo init -u https://aosp.tuna.tsinghua.edu.cn/platform/manifest

**如果提示无法连接到 gerrit.googlesource.com，请参照[git-repo的帮助页面](/help/git-repo)的更新一节。**

如果需要某个特定的 Android 版本([列表](https://source.android.com/source/build-numbers.html#source-code-tags-and-builds))：

    repo init -u https://aosp.tuna.tsinghua.edu.cn/platform/manifest -b android-4.0.1_r1

同步源码树（以后只需执行这条命令来同步）：

    repo sync

### 建立次级镜像 {#section-3}

由于 AOSP 镜像需求量巨大，且 Git 服务占资源较多，TUNA 服务器因 AOSP 产生的负载已经占主要部分。 如果你是团队用户，我们强烈建议你通过 TUNA 建立次级镜像，再分享给团队内其他用户，减轻 TUNA 服务器压力。 建立 AOSP 镜像需要占用约 80G 磁盘。

具体步骤为:

下载 `repo` 工具和建立工作目录（略）

初始化:

    repo init -u https://aosp.tuna.tsinghua.edu.cn/mirror/manifest --mirror

最后同步源码树:

    repo sync

同步完成后，运行 `git daemon --verbose --export-all  --base-path=WORKING_DIR WORKING_DIR` (`WORKING_DIR`为代码树所在目录) 。

此后，其他用户使用 `git://ip.to.mirror/` 作为镜像即可。

### 替换已有的 AOSP 源代码的 remote {#aosp--remote}

如果你之前已经通过某种途径获得了 AOSP 的源码(或者你只是 init 这一步完成后)， 你希望以后通过 TUNA 同步 AOSP 部分的代码，只需要将 `.repo/manifest.xml` 把其中的 aosp 这个 remote 的 fetch 从 `https://android.googlesource.com` 改为 `https://aosp.tuna.tsinghua.edu.cn/`。

    <manifest>

       <remote  name="aosp"
    -           fetch="https://android.googlesource.com"
    +           fetch="https://aosp.tuna.tsinghua.edu.cn"
                review="android-review.googlesource.com" />

       <remote  name="github"

同时，修改 `.repo/manifests.git/config`，将

    url = https://android.googlesource.com/platform/manifest

更改为

    url = https://aosp.tuna.tsinghua.edu.cn/platform/manifest

**这个方法也可以用来在同步 Cyanogenmod 代码的时候从 TUNA 同步部分代码**

### FAQ

1.  镜像的是什么？
    -   AOSP 的 git 仓库
2.  为何不能通过浏览器访问？
    -   暂时没有 gitweb, 而且反正是 git bare 仓库，没有可以直接看到的内容。
3.  出现 `curl: (22) The requested URL returned error: 404 Not Found Server does not provide clone.bundle; ignoring.` 怎么办？
    -   无视即可。

AUR 镜像使用帮助 {#aur-}
================

修改 `/etc/yaourtrc`，去掉 `# AURURL` 的注释，修改为

    AURURL="https://aur.tuna.tsinghua.edu.cn"

CocoaPods 镜像使用帮助 {#cocoapods-}
----------------------

CocoaPods 是一个 Cocoa 和 Cocoa Touch 框架的依赖管理器，具体原理和 Homebrew 有点类似，都是从 GitHub 下载索引，然后根据索引下载依赖的源代码。

对于旧版的 CocoaPods 可以使用如下方法使用 tuna 的镜像：

    $ pod repo remove master
    $ pod repo add master https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git
    $ pod repo update

新版的 CocoaPods 不允许用`pod repo add`直接添加master库了，但是依然可以：

    $ cd ~/.cocoapods/repos 
    $ pod repo remove master
    $ git clone https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git master

最后进入自己的工程，在自己工程的`podFile`第一行加上：

    source 'https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git'

Android 镜像使用帮助 {#android-}
--------------------

**注意: 本镜像是 AOSP 镜像，Android SDK因版权原因，我们不能提供镜像服务。**

参考 Google 教程 <https://source.android.com/source/downloading.html>， 将 `https://android.googlesource.com/` 全部使用 `https://aosp.tuna.tsinghua.edu.cn/` 代替即可。

由于使用 HTTPS 协议更安全，并且更便于我们灵活处理，所以强烈推荐使用 HTTPS 协议同步 AOSP 镜像。

**由于 AOSP 镜像造成CPU/内存负载过重，我们限制了并发数量，请尽量错峰(凌晨)同步。**

-   **2016-06-24 : 关闭 git:// 协议，仅支持 HTTPS**
-   **2016-04-03 : 删除每月初始化包中的冗余内容，使用方法更新**
-   **2015-12-21 : 增加每月初始化包，少量修正文档错误**
-   **2015-10-13 : 修复上游替换文档错误**
-   **2015-10-13 : 修复次级镜像文档错误**
-   **2015-10-09 : 恢复 git://aosp.tuna.tsinghua.edu.cn/aosp/ 访问**
-   **2015-10-08 : 镜像地址更新为 https://aosp.tuna.tsinghua.edu.cn/ (结尾没有/android)**

### 过程摘录 {#section}

(参考 <https://lug.ustc.edu.cn/wiki/mirrors/help/aosp> 编写)

下载 repo 工具:

    mkdir ~/bin
    PATH=~/bin:$PATH
    curl https://storage.googleapis.com/git-repo-downloads/repo > ~/bin/repo
    chmod a+x ~/bin/repo

或者使用tuna的[git-repo镜像](https://mirrors.tuna.tsinghua.edu.cn/help/git-repo/)

#### 使用每月更新的初始化包 {#section-1}

由于首次同步需要下载 24GB 数据，过程中任何网络故障都可能造成同步失败，我们强烈建议您使用初始化包进行初始化。

下载 <https://mirrors.tuna.tsinghua.edu.cn/aosp-monthly/aosp-latest.tar>，下载完成后记得根据 checksum.txt 的内容校验一下。

由于所有代码都是从隐藏的 `.repo` 目录中 checkout 出来的，所以我们只保留了 `.repo` 目录，下载后解压 再 `repo sync` 一遍即可得到完整的目录。

使用方法如下:

    wget https://mirrors.tuna.tsinghua.edu.cn/aosp-monthly/aosp-latest.tar # 下载初始化包
    tar xf aosp-latest.tar
    cd AOSP   # 解压得到的 AOSP 工程目录
    # 这时 ls 的话什么也看不到，因为只有一个隐藏的 .repo 目录
    repo sync # 正常同步一遍即可得到完整目录
    # 或 repo sync -l 仅checkout代码

此后，每次只需运行 `repo sync` 即可保持同步。 **我们强烈建议您保持每天同步，并尽量选择凌晨等低峰时间**

#### 传统初始化方法 {#section-2}

建立工作目录:

    mkdir WORKING_DIRECTORY
    cd WORKING_DIRECTORY

初始化仓库:

    repo init -u https://aosp.tuna.tsinghua.edu.cn/platform/manifest

**如果提示无法连接到 gerrit.googlesource.com，请参照[git-repo的帮助页面](/help/git-repo)的更新一节。**

如果需要某个特定的 Android 版本([列表](https://source.android.com/source/build-numbers.html#source-code-tags-and-builds))：

    repo init -u https://aosp.tuna.tsinghua.edu.cn/platform/manifest -b android-4.0.1_r1

同步源码树（以后只需执行这条命令来同步）：

    repo sync

### 建立次级镜像 {#section-3}

由于 AOSP 镜像需求量巨大，且 Git 服务占资源较多，TUNA 服务器因 AOSP 产生的负载已经占主要部分。 如果你是团队用户，我们强烈建议你通过 TUNA 建立次级镜像，再分享给团队内其他用户，减轻 TUNA 服务器压力。 建立 AOSP 镜像需要占用约 80G 磁盘。

具体步骤为:

下载 `repo` 工具和建立工作目录（略）

初始化:

    repo init -u https://aosp.tuna.tsinghua.edu.cn/mirror/manifest --mirror

最后同步源码树:

    repo sync

同步完成后，运行 `git daemon --verbose --export-all  --base-path=WORKING_DIR WORKING_DIR` (`WORKING_DIR`为代码树所在目录) 。

此后，其他用户使用 `git://ip.to.mirror/` 作为镜像即可。

### 替换已有的 AOSP 源代码的 remote {#aosp--remote}

如果你之前已经通过某种途径获得了 AOSP 的源码(或者你只是 init 这一步完成后)， 你希望以后通过 TUNA 同步 AOSP 部分的代码，只需要将 `.repo/manifest.xml` 把其中的 aosp 这个 remote 的 fetch 从 `https://android.googlesource.com` 改为 `https://aosp.tuna.tsinghua.edu.cn/`。

    <manifest>

       <remote  name="aosp"
    -           fetch="https://android.googlesource.com"
    +           fetch="https://aosp.tuna.tsinghua.edu.cn"
                review="android-review.googlesource.com" />

       <remote  name="github"

同时，修改 `.repo/manifests.git/config`，将

    url = https://android.googlesource.com/platform/manifest

更改为

    url = https://aosp.tuna.tsinghua.edu.cn/platform/manifest

**这个方法也可以用来在同步 Cyanogenmod 代码的时候从 TUNA 同步部分代码**

### FAQ {#faq}

1.  镜像的是什么？
    -   AOSP 的 git 仓库
2.  为何不能通过浏览器访问？
    -   暂时没有 gitweb, 而且反正是 git bare 仓库，没有可以直接看到的内容。
3.  出现 `curl: (22) The requested URL returned error: 404 Not Found Server does not provide clone.bundle; ignoring.` 怎么办？
    -   无视即可。

AUR 镜像使用帮助 {#aur-}
================

修改 `/etc/yaourtrc`，去掉 `# AURURL` 的注释，修改为

    AURURL="https://aur.tuna.tsinghua.edu.cn"

CocoaPods 镜像使用帮助 {#cocoapods-}
----------------------

CocoaPods 是一个 Cocoa 和 Cocoa Touch 框架的依赖管理器，具体原理和 Homebrew 有点类似，都是从 GitHub 下载索引，然后根据索引下载依赖的源代码。

对于旧版的 CocoaPods 可以使用如下方法使用 tuna 的镜像：

    $ pod repo remove master
    $ pod repo add master https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git
    $ pod repo update

新版的 CocoaPods 不允许用`pod repo add`直接添加master库了，但是依然可以：

    $ cd ~/.cocoapods/repos 
    $ pod repo remove master
    $ git clone https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git master

最后进入自己的工程，在自己工程的`podFile`第一行加上：

    source 'https://mirrors.tuna.tsinghua.edu.cn/git/CocoaPods/Specs.git'
