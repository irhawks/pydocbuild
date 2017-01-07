[](#section){.anchor-link}语义化版本 2.0.0 {#section}
==========================================

[](#section-1){.anchor-link}摘要 {#section-1}
--------------------------------

版本格式：主版本号.次版本号.修订号，版本号递增规则如下：

1.  主版本号：当你做了不兼容的 API 修改，
2.  次版本号：当你做了向下兼容的功能性新增，
3.  修订号：当你做了向下兼容的问题修正。

先行版本号及版本编译信息可以加到“主版本号.次版本号.修订号”的后面，作为延伸。

[](#section-2){.anchor-link}简介 {#section-2}
--------------------------------

在软件管理的领域里存在着被称作“依赖地狱”的死亡之谷，系统规模越大，加入的套件越多，你就越有可能在未来的某一天发现自己已深陷绝望之中。

在依赖高的系统中发布新版本套件可能很快会成为恶梦。如果依赖关系过高，可能面临版本控制被锁死的风险（必须对每一个相依套件改版才能完成某次升级）。而如果依赖关系过于松散，又将无法避免版本的混乱（假设兼容于未来的多个版本已超出了合理数量）。当你专案的进展因为版本相依被锁死或版本混乱变得不够简便和可靠，就意味着你正处于依赖地狱之中。

作为这个问题的解决方案之一，我提议用一组简单的规则及条件来约束版本号的配置和增长。这些规则是根据（但不局限于）已经被各种封闭、开放源码软件所广泛使用的惯例所设计。为了让这套理论运作，你必须先有定义好的公共 API 。这可以透过文件定义或代码强制要求来实现。无论如何，这套 API 的清楚明了是十分重要的。一旦你定义了公共 API，你就可以透过修改相应的版本号来向大家说明你的修改。考虑使用这样的版本号格式：XYZ （主版本号.次版本号.修订号）修复问题但不影响API 时，递增修订号；API 保持向下兼容的新增及修改时，递增次版本号；进行不向下兼容的修改时，递增主版本号。

我称这套系统为“语义化的版本控制”，在这套约定下，版本号及其更新方式包含了相邻版本间的底层代码和修改内容的信息。

[](#semver){.anchor-link}语义化版本控制规范（SemVer） {#semver}
-----------------------------------------------------

以下关键词 MUST、MUST NOT、REQUIRED、SHALL、SHALL NOT、SHOULD、SHOULD NOT、 RECOMMENDED、MAY、OPTIONAL 依照 RFC 2119 的叙述解读。（译注：为了保持语句顺畅， 以下文件遇到的关键词将依照整句语义进行翻译，在此先不进行个别翻译。）

1.  <div id="spec-item-1">

    </div>

    [](#spec-item-1){.anchor-link}

    使用语义化版本控制的软件“必须 MUST ”定义公共 API。该 API 可以在代码中被定义或出现于严谨的文件内。无论何种形式都应该力求精确且完整。

2.  <div id="spec-item-2">

    </div>

    [](#spec-item-2){.anchor-link}

    标准的版本号“必须 MUST ”采用 XYZ 的格式，其中 X、Y 和 Z 为非负的整数，且“禁止 MUST NOT”在数字前方补零。X 是主版本号、Y 是次版本号、而 Z 为修订号。每个元素“必须 MUST ”以数值来递增。例如：1.9.1 -&gt; 1.10.0 -&gt; 1.11.0。

3.  <div id="spec-item-3">

    </div>

    [](#spec-item-3){.anchor-link}

    标记版本号的软件发行后，“禁止 MUST NOT ”改变该版本软件的内容。任何修改都“必须 MUST ”以新版本发行。

4.  <div id="spec-item-4">

    </div>

    [](#spec-item-4){.anchor-link}

    主版本号为零（0.y.z）的软件处于开发初始阶段，一切都可能随时被改变。这样的公共 API 不应该被视为稳定版。

5.  <div id="spec-item-5">

    </div>

    [](#spec-item-5){.anchor-link}

    1.0.0 的版本号用于界定公共 API 的形成。这一版本之后所有的版本号更新都基于公共 API 及其修改内容。

6.  <div id="spec-item-6">

    </div>

    [](#spec-item-6){.anchor-link}

    修订号 Z（x.y.Z `|`{.highlighter-rouge} x &gt; 0）“必须 MUST ”在只做了向下兼容的修正时才递增。这里的修正指的是针对不正确结果而进行的内部修改。

7.  <div id="spec-item-7">

    </div>

    [](#spec-item-7){.anchor-link}

    次版本号 Y（x.Y.z `|`{.highlighter-rouge} x &gt; 0）“必须 MUST ”在有向下兼容的新功能出现时递增。在任何公共 API 的功能被标记为弃用时也“必须 MUST ”递增。也“可以 MAY ”在内部程序有大量新功能或改进被加入时递增，其中“可以 MAY ”包括修订级别的改变。每当次版本号递增时，修订号“必须 MUST ”归零。

8.  <div id="spec-item-8">

    </div>

    [](#spec-item-8){.anchor-link}

    主版本号 X（X.y.z `|`{.highlighter-rouge} X &gt; 0）“必须 MUST ”在有任何不兼容的修改被加入公共 API 时递增。其中“可以 MAY ”包括次版本号及修订级别的改变。每当主版本号递增时，次版本号和修订号“必须 MUST ”归零。

9.  <div id="spec-item-9">

    </div>

    [](#spec-item-9){.anchor-link}

    先行版本号“可以 MAY ”被标注在修订版之后，先加上一个连接号再加上一连串以句点分隔的标识符号来修饰。标识符号“必须 MUST ”由 ASCII 码的英数字和连接号 \[0-9A-Za-z-\] 组成，且“禁止 MUST NOT ”留白。数字型的标识符号“禁止 MUST NOT ”在前方补零。先行版的优先级低于相关联的标准版本。被标上先行版本号则表示这个版本并非稳定而且可能无法达到兼容的需求。范例：1.0.0-alpha、1.0.0-alpha.1、1.0.0-0.3.7、1.0.0-x.7.z.92。

10. <div id="spec-item-10">

    </div>

    [](#spec-item-10){.anchor-link}

    版本编译信息“可以 MAY ”被标注在修订版或先行版本号之后，先加上一个加号再加上一连串以句点分隔的标识符号来修饰。标识符号“必须 MUST ”由 ASCII 的英数字和连接号 \[0-9A-Za-z-\] 组成，且“禁止 MUST NOT ”留白。当判断版本的优先层级时，版本编译信息“可 SHOULD ”被忽略。因此当两个版本只有在版本编译信息有差别时，属于相同的优先层级。范例：1.0.0-alpha+001、1.0.0+20130313144700、1.0.0-beta+exp.sha.5114f85。

11. <div id="spec-item-11">

    </div>

    [](#spec-item-11){.anchor-link}

    版本的优先层级指的是不同版本在排序时如何比较。判断优先层级时，“必须 MUST ”把版本依序拆分为主版本号、次版本号、修订号及先行版本号后进行比较（版本编译信息不在这份比较的列表中）。由左到右依序比较每个标识符号，第一个差异值用来决定优先层级：主版本号、次版本号及修订号以数值比较，例如：1.0.0 &lt; 2.0.0 &lt; 2.1.0 &lt; 2.1.1。当主版本号、次版本号及修订号都相同时，改以优先层级比较低的先行版本号决定。例如：1.0.0-alpha &lt; 1.0.0。有相同主版本号、次版本号及修订号的两个先行版本号，其优先层级“必须 MUST ”透过由左到右的每个被句点分隔的标识符号来比较，直到找到一个差异值后决定：只有数字的标识符号以数值高低比较，有字母或连接号时则逐字以 ASCII 的排序来比较。数字的标识符号比非数字的标识符号优先层级低。若开头的标识符号都相同时，栏位比较多的先行版本号优先层级比较高。范例：1.0.0-alpha &lt; 1.0.0-alpha.1 &lt; 1.0.0-alpha.beta &lt; 1.0.0-beta &lt; 1.0.0-beta.2 &lt; 1.0.0-beta.11 &lt; 1.0.0- rc.1 &lt; 1.0.0。

[](#section-3){.anchor-link}为什么要使用语义化的版本控制？ {#section-3}
----------------------------------------------------------

这并不是一个新的或者革命性的想法。实际上，你可能已经在做一些近似的事情了。问题在于只是“近似”还不够。如果没有某个正式的规范可循，版本号对于依赖的管理并无实质意义。将上述的想法命名并给予清楚的定义，让你对软件使用者传达意向变得容易。一旦这些意向变得清楚，弹性（但又不会太弹性）的依赖规范就能达成。

举个简单的例子就可以展示语义化的版本控制如何让依赖地狱成为过去。假设有个名为“救火车”的函式库，它需要另一个名为“梯子”并已经有使用语义化版本控制的套件。当救火车创建时，梯子的版本号为 3.1.0。因为救火车使用了一些版本 3.1.0 所新增的功能， 你可以放心地指定相依于梯子的版本号大等于 3.1.0 但小于 4.0.0。这样，当梯子版本 3.1.1 和 3.2.0 发布时，你可以将直接它们纳入你的套件管理系统，因为它们能与原有相依的软件兼容。

作为一位负责任的开发者，你理当确保每次套件升级的运作与版本号的表述一致。现实世界是复杂的，我们除了提高警觉外能做的不多。你所能做的就是让语义化的版本控制为你提供一个健全的方式来发行以及升级套件，而无需推出新的相依套件，节省你的时间及烦恼。

如果你对此认同，希望立即开始使用语义化版本控制，你只需声明你的函式库正在使用它并遵循这些规则就可以了。请在你的 README 文件中保留此页连结，让别人也知道这些规则并从中受益。

[](#faq){.anchor-link}FAQ
-------------------------

### [](#yz-){.anchor-link}在 0.y.z 初始开发阶段，我该如何进行版本控制？ {#yz-}

最简单的做法是以 0.1.0 作为你的初始化开发版本，并在后续的每次发行时递增次版本号。

### [](#section-4){.anchor-link}如何判断发布 1.0.0 版本的时机？ {#section-4}

当你的软件被用于正式环境，它应该已经达到了 1.0.0 版。如果你已经有个稳定的 API 被使用者依赖，也会是 1.0.0 版。如果你很担心向下兼容的问题，也应该算是 1.0.0 版了。

### [](#section-5){.anchor-link}这不会阻碍快速开发和迭代吗？ {#section-5}

主版本号为零的时候就是为了做快速开发。如果你每天都在改变 API，那么你应该仍在主版本号为零的阶段（0.y.z），或是正在下个主版本的独立开发分支中。

### [](#api-4200-){.anchor-link}对于公共 API，若即使是最小但不向下兼容的改变都需要产生新的主版本号，岂不是很快就达到 42.0.0 版？ {#api-4200-}

这是开发的责任感和前瞻性的问题。不兼容的改变不应该轻易被加入到有许多依赖代码的软件中。升级所付出的代价可能是巨大的。要递增主版本号来发行不兼容的改版，意味着你必须为这些改变所带来的影响深思熟虑，并且评估所涉及的成本及效益比。

### [](#api-){.anchor-link}为整个公共 API 写文件太费事了！ {#api-}

为供他人使用的软件编写适当的文件，是你作为一名专业开发者应尽的职责。保持专案高效一个非常重要的部份是掌控软件的复杂度，如果没有人知道如何使用你的软件或不知道哪些函数的调用是可靠的，要掌控复杂度会是困难的。长远来看，使用语义化版本控制以及对于公共 API 有良好规范的坚持，可以让每个人及每件事都运行顺畅。

### [](#section-6){.anchor-link}万一不小心把一个不兼容的改版当成了次版本号发行了该怎么办？ {#section-6}

一旦发现自己破坏了语义化版本控制的规范，就要修正这个问题，并发行一个新的次版本号来更正这个问题并且恢复向下兼容。即使是这种情况，也不能去修改已发行的版本。可以的话，将有问题的版本号记录到文件中，告诉使用者问题所在，让他们能够意识到这是有问题的版本。

### [](#api--1){.anchor-link}如果我更新了自己的依赖但没有改变公共 API 该怎么办？ {#api--1}

由于没有影响到公共 API，这可以被认定是兼容的。若某个软件和你的套件有共同依赖，则它会有自己的依赖规范，作者也会告知可能的冲突。要判断改版是属于修订等级或是次版等级，是依据你更新的依赖关系是为了修复问题或是加入新功能。对于后者，我经常会预期伴随着更多的代码，这显然会是一个次版本号级别的递增。

### [](#api--2){.anchor-link}如果我变更了公共 API 但无意中未遵循版本号的改动怎么办呢？（意即在修订等级的发布中，误将重大且不兼容的改变加到代码之中） {#api--2}

自行做最佳的判断。如果你有庞大的使用者群在依照公共 API 的意图而变更行为后会大受影响，那么最好做一次主版本的发布，即使严格来说这个修复仅是修订等级的发布。记住， 语义化的版本控制就是透过版本号的改变来传达意义。若这些改变对你的使用者是重要的，那就透过版本号来向他们说明。

### [](#section-7){.anchor-link}我该如何处理即将弃用的功能？ {#section-7}

弃用现存的功能是软件开发中的家常便饭，也通常是向前发展所必须的。当你弃用部份公共 API 时，你应该做两件事：（1）更新你的文件让使用者知道这个改变，（2）在适当的时机将弃用的功能透过新的次版本号发布。在新的主版本完全移除弃用功能前，至少要有一个次版本包含这个弃用信息，这样使用者才能平顺地转移到新版 API。

### [](#section-8){.anchor-link}语义化版本对于版本的字串长度是否有限制呢？ {#section-8}

没有，请自行做适当的判断。举例来说，长到 255 个字元的版本已过度夸张。再者，特定的系统对于字串长度可能会有他们自己的限制。

[](#section-9){.anchor-link}关于 {#section-9}
--------------------------------

语义化版本控制的规范是由 Gravatars 创办者兼 GitHub 共同创办者 [Tom Preston-Werner](http://tom.preston-werner.com) 所建立。

如果您有任何建议，请到 [GitHub 上提出您的问题](https://github.com/mojombo/semver/issues)。

[](#section-10){.anchor-link}授权 {#section-10}
---------------------------------

创用 CC 姓名标示 3.0 Unported 授权条款 http://creativecommons.org/licenses/by/3.0/

[](#semantic-versioning-200){.anchor-link}Semantic Versioning 2.0.0 {#semantic-versioning-200}
===================================================================

[](#summary){.anchor-link}Summary
---------------------------------

Given a version number MAJOR.MINOR.PATCH, increment the:

1.  MAJOR version when you make incompatible API changes,
2.  MINOR version when you add functionality in a backwards-compatible manner, and
3.  PATCH version when you make backwards-compatible bug fixes.

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

[](#introduction){.anchor-link}Introduction
-------------------------------------------

In the world of software management there exists a dread place called “dependency hell.” The bigger your system grows and the more packages you integrate into your software, the more likely you are to find yourself, one day, in this pit of despair.

In systems with many dependencies, releasing new package versions can quickly become a nightmare. If the dependency specifications are too tight, you are in danger of version lock (the inability to upgrade a package without having to release new versions of every dependent package). If dependencies are specified too loosely, you will inevitably be bitten by version promiscuity (assuming compatibility with more future versions than is reasonable). Dependency hell is where you are when version lock and/or version promiscuity prevent you from easily and safely moving your project forward.

As a solution to this problem, I propose a simple set of rules and requirements that dictate how version numbers are assigned and incremented. These rules are based on but not necessarily limited to pre-existing widespread common practices in use in both closed and open-source software. For this system to work, you first need to declare a public API. This may consist of documentation or be enforced by the code itself. Regardless, it is important that this API be clear and precise. Once you identify your public API, you communicate changes to it with specific increments to your version number. Consider a version format of X.Y.Z (Major.Minor.Patch). Bug fixes not affecting the API increment the patch version, backwards compatible API additions/changes increment the minor version, and backwards incompatible API changes increment the major version.

I call this system “Semantic Versioning.” Under this scheme, version numbers and the way they change convey meaning about the underlying code and what has been modified from one version to the next.

[](#semantic-versioning-specification-semver){.anchor-link}Semantic Versioning Specification (SemVer)
-----------------------------------------------------------------------------------------------------

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [RFC 2119](http://tools.ietf.org/html/rfc2119).

1.  <div id="spec-item-1">

    </div>

    [](#spec-item-1){.anchor-link}

    Software using Semantic Versioning MUST declare a public API. This API could be declared in the code itself or exist strictly in documentation. However it is done, it should be precise and comprehensive.

2.  <div id="spec-item-2">

    </div>

    [](#spec-item-2){.anchor-link}

    A normal version number MUST take the form X.Y.Z where X, Y, and Z are non-negative integers, and MUST NOT contain leading zeroes. X is the major version, Y is the minor version, and Z is the patch version. Each element MUST increase numerically. For instance: 1.9.0 -&gt; 1.10.0 -&gt; 1.11.0.

3.  <div id="spec-item-3">

    </div>

    [](#spec-item-3){.anchor-link}

    Once a versioned package has been released, the contents of that version MUST NOT be modified. Any modifications MUST be released as a new version.

4.  <div id="spec-item-4">

    </div>

    [](#spec-item-4){.anchor-link}

    Major version zero (0.y.z) is for initial development. Anything may change at any time. The public API should not be considered stable.

5.  <div id="spec-item-5">

    </div>

    [](#spec-item-5){.anchor-link}

    Version 1.0.0 defines the public API. The way in which the version number is incremented after this release is dependent on this public API and how it changes.

6.  <div id="spec-item-6">

    </div>

    [](#spec-item-6){.anchor-link}

    Patch version Z (x.y.Z | x &gt; 0) MUST be incremented if only backwards compatible bug fixes are introduced. A bug fix is defined as an internal change that fixes incorrect behavior.

7.  <div id="spec-item-7">

    </div>

    [](#spec-item-7){.anchor-link}

    Minor version Y (x.Y.z | x &gt; 0) MUST be incremented if new, backwards compatible functionality is introduced to the public API. It MUST be incremented if any public API functionality is marked as deprecated. It MAY be incremented if substantial new functionality or improvements are introduced within the private code. It MAY include patch level changes. Patch version MUST be reset to 0 when minor version is incremented.

8.  <div id="spec-item-8">

    </div>

    [](#spec-item-8){.anchor-link}

    Major version X (X.y.z | X &gt; 0) MUST be incremented if any backwards incompatible changes are introduced to the public API. It MAY include minor and patch level changes. Patch and minor version MUST be reset to 0 when major version is incremented.

9.  <div id="spec-item-9">

    </div>

    [](#spec-item-9){.anchor-link}

    A pre-release version MAY be denoted by appending a hyphen and a series of dot separated identifiers immediately following the patch version. Identifiers MUST comprise only ASCII alphanumerics and hyphen \[0-9A-Za-z-\]. Identifiers MUST NOT be empty. Numeric identifiers MUST NOT include leading zeroes. Pre-release versions have a lower precedence than the associated normal version. A pre-release version indicates that the version is unstable and might not satisfy the intended compatibility requirements as denoted by its associated normal version. Examples: 1.0.0-alpha, 1.0.0-alpha.1, 1.0.0-0.3.7, 1.0.0-x.7.z.92.

10. <div id="spec-item-10">

    </div>

    [](#spec-item-10){.anchor-link}

    Build metadata MAY be denoted by appending a plus sign and a series of dot separated identifiers immediately following the patch or pre-release version. Identifiers MUST comprise only ASCII alphanumerics and hyphen \[0-9A-Za-z-\]. Identifiers MUST NOT be empty. Build metadata SHOULD be ignored when determining version precedence. Thus two versions that differ only in the build metadata, have the same precedence. Examples: 1.0.0-alpha+001, 1.0.0+20130313144700, 1.0.0-beta+exp.sha.5114f85.

11. <div id="spec-item-11">

    </div>

    [](#spec-item-11){.anchor-link}

    Precedence refers to how versions are compared to each other when ordered. Precedence MUST be calculated by separating the version into major, minor, patch and pre-release identifiers in that order (Build metadata does not figure into precedence). Precedence is determined by the first difference when comparing each of these identifiers from left to right as follows: Major, minor, and patch versions are always compared numerically. Example: 1.0.0 &lt; 2.0.0 &lt; 2.1.0 &lt; 2.1.1. When major, minor, and patch are equal, a pre-release version has lower precedence than a normal version. Example: 1.0.0-alpha &lt; 1.0.0. Precedence for two pre-release versions with the same major, minor, and patch version MUST be determined by comparing each dot separated identifier from left to right until a difference is found as follows: identifiers consisting of only digits are compared numerically and identifiers with letters or hyphens are compared lexically in ASCII sort order. Numeric identifiers always have lower precedence than non-numeric identifiers. A larger set of pre-release fields has a higher precedence than a smaller set, if all of the preceding identifiers are equal. Example: 1.0.0-alpha &lt; 1.0.0-alpha.1 &lt; 1.0.0-alpha.beta &lt; 1.0.0-beta &lt; 1.0.0-beta.2 &lt; 1.0.0-beta.11 &lt; 1.0.0-rc.1 &lt; 1.0.0.

[](#why-use-semantic-versioning){.anchor-link}Why Use Semantic Versioning?
--------------------------------------------------------------------------

This is not a new or revolutionary idea. In fact, you probably do something close to this already. The problem is that “close” isn’t good enough. Without compliance to some sort of formal specification, version numbers are essentially useless for dependency management. By giving a name and clear definition to the above ideas, it becomes easy to communicate your intentions to the users of your software. Once these intentions are clear, flexible (but not too flexible) dependency specifications can finally be made.

A simple example will demonstrate how Semantic Versioning can make dependency hell a thing of the past. Consider a library called “Firetruck.” It requires a Semantically Versioned package named “Ladder.” At the time that Firetruck is created, Ladder is at version 3.1.0. Since Firetruck uses some functionality that was first introduced in 3.1.0, you can safely specify the Ladder dependency as greater than or equal to 3.1.0 but less than 4.0.0. Now, when Ladder version 3.1.1 and 3.2.0 become available, you can release them to your package management system and know that they will be compatible with existing dependent software.

As a responsible developer you will, of course, want to verify that any package upgrades function as advertised. The real world is a messy place; there’s nothing we can do about that but be vigilant. What you can do is let Semantic Versioning provide you with a sane way to release and upgrade packages without having to roll new versions of dependent packages, saving you time and hassle.

If all of this sounds desirable, all you need to do to start using Semantic Versioning is to declare that you are doing so and then follow the rules. Link to this website from your README so others know the rules and can benefit from them.

[](#faq){.anchor-link}FAQ {#faq}
-------------------------

### [](#how-should-i-deal-with-revisions-in-the-0yz-initial-development-phase){.anchor-link}How should I deal with revisions in the 0.y.z initial development phase? {#how-should-i-deal-with-revisions-in-the-0yz-initial-development-phase}

The simplest thing to do is start your initial development release at 0.1.0 and then increment the minor version for each subsequent release.

### [](#how-do-i-know-when-to-release-100){.anchor-link}How do I know when to release 1.0.0? {#how-do-i-know-when-to-release-100}

If your software is being used in production, it should probably already be 1.0.0. If you have a stable API on which users have come to depend, you should be 1.0.0. If you’re worrying a lot about backwards compatibility, you should probably already be 1.0.0.

### [](#doesnt-this-discourage-rapid-development-and-fast-iteration){.anchor-link}Doesn’t this discourage rapid development and fast iteration?

Major version zero is all about rapid development. If you’re changing the API every day you should either still be in version 0.y.z or on a separate development branch working on the next major version.

### [](#if-even-the-tiniest-backwards-incompatible-changes-to-the-public-api-require-a-major-version-bump-wont-i-end-up-at-version-4200-very-rapidly){.anchor-link}If even the tiniest backwards incompatible changes to the public API require a major version bump, won’t I end up at version 42.0.0 very rapidly? {#if-even-the-tiniest-backwards-incompatible-changes-to-the-public-api-require-a-major-version-bump-wont-i-end-up-at-version-4200-very-rapidly}

This is a question of responsible development and foresight. Incompatible changes should not be introduced lightly to software that has a lot of dependent code. The cost that must be incurred to upgrade can be significant. Having to bump major versions to release incompatible changes means you’ll think through the impact of your changes, and evaluate the cost/benefit ratio involved.

### [](#documenting-the-entire-public-api-is-too-much-work){.anchor-link}Documenting the entire public API is too much work!

It is your responsibility as a professional developer to properly document software that is intended for use by others. Managing software complexity is a hugely important part of keeping a project efficient, and that’s hard to do if nobody knows how to use your software, or what methods are safe to call. In the long run, Semantic Versioning, and the insistence on a well defined public API can keep everyone and everything running smoothly.

### [](#what-do-i-do-if-i-accidentally-release-a-backwards-incompatible-change-as-a-minor-version){.anchor-link}What do I do if I accidentally release a backwards incompatible change as a minor version?

As soon as you realize that you’ve broken the Semantic Versioning spec, fix the problem and release a new minor version that corrects the problem and restores backwards compatibility. Even under this circumstance, it is unacceptable to modify versioned releases. If it’s appropriate, document the offending version and inform your users of the problem so that they are aware of the offending version.

### [](#what-should-i-do-if-i-update-my-own-dependencies-without-changing-the-public-api){.anchor-link}What should I do if I update my own dependencies without changing the public API?

That would be considered compatible since it does not affect the public API. Software that explicitly depends on the same dependencies as your package should have their own dependency specifications and the author will notice any conflicts. Determining whether the change is a patch level or minor level modification depends on whether you updated your dependencies in order to fix a bug or introduce new functionality. I would usually expect additional code for the latter instance, in which case it’s obviously a minor level increment.

### [](#what-if-i-inadvertently-alter-the-public-api-in-a-way-that-is-not-compliant-with-the-version-number-change-ie-the-code-incorrectly-introduces-a-major-breaking-change-in-a-patch-release){.anchor-link}What if I inadvertently alter the public API in a way that is not compliant with the version number change (i.e. the code incorrectly introduces a major breaking change in a patch release) {#what-if-i-inadvertently-alter-the-public-api-in-a-way-that-is-not-compliant-with-the-version-number-change-ie-the-code-incorrectly-introduces-a-major-breaking-change-in-a-patch-release}

Use your best judgment. If you have a huge audience that will be drastically impacted by changing the behavior back to what the public API intended, then it may be best to perform a major version release, even though the fix could strictly be considered a patch release. Remember, Semantic Versioning is all about conveying meaning by how the version number changes. If these changes are important to your users, use the version number to inform them.

### [](#how-should-i-handle-deprecating-functionality){.anchor-link}How should I handle deprecating functionality?

Deprecating existing functionality is a normal part of software development and is often required to make forward progress. When you deprecate part of your public API, you should do two things: (1) update your documentation to let users know about the change, (2) issue a new minor release with the deprecation in place. Before you completely remove the functionality in a new major release there should be at least one minor release that contains the deprecation so that users can smoothly transition to the new API.

### [](#does-semver-have-a-size-limit-on-the-version-string){.anchor-link}Does semver have a size limit on the version string?

No, but use good judgment. A 255 character version string is probably overkill, for example. Also, specific systems may impose their own limits on the size of the string.

[](#about){.anchor-link}About
-----------------------------

The Semantic Versioning specification is authored by [Tom Preston-Werner](http://tom.preston-werner.com), inventor of Gravatars and cofounder of GitHub.

If you’d like to leave feedback, please [open an issue on GitHub](https://github.com/mojombo/semver/issues).

[](#license){.anchor-link}License
---------------------------------

[Creative Commons - CC BY 3.0](http://creativecommons.org/licenses/by/3.0/)

[](#section){.anchor-link}语义化版本 2.0.0 {#section}
==========================================

[](#section-1){.anchor-link}摘要 {#section-1}
--------------------------------

版本格式：主版本号.次版本号.修订号，版本号递增规则如下：

1.  主版本号：当你做了不兼容的 API 修改，
2.  次版本号：当你做了向下兼容的功能性新增，
3.  修订号：当你做了向下兼容的问题修正。

先行版本号及版本编译信息可以加到“主版本号.次版本号.修订号”的后面，作为延伸。

[](#section-2){.anchor-link}简介 {#section-2}
--------------------------------

在软件管理的领域里存在着被称作“依赖地狱”的死亡之谷，系统规模越大，加入的套件越多，你就越有可能在未来的某一天发现自己已深陷绝望之中。

在依赖高的系统中发布新版本套件可能很快会成为恶梦。如果依赖关系过高，可能面临版本控制被锁死的风险（必须对每一个相依套件改版才能完成某次升级）。而如果依赖关系过于松散，又将无法避免版本的混乱（假设兼容于未来的多个版本已超出了合理数量）。当你专案的进展因为版本相依被锁死或版本混乱变得不够简便和可靠，就意味着你正处于依赖地狱之中。

作为这个问题的解决方案之一，我提议用一组简单的规则及条件来约束版本号的配置和增长。这些规则是根据（但不局限于）已经被各种封闭、开放源码软件所广泛使用的惯例所设计。为了让这套理论运作，你必须先有定义好的公共 API 。这可以透过文件定义或代码强制要求来实现。无论如何，这套 API 的清楚明了是十分重要的。一旦你定义了公共 API，你就可以透过修改相应的版本号来向大家说明你的修改。考虑使用这样的版本号格式：XYZ （主版本号.次版本号.修订号）修复问题但不影响API 时，递增修订号；API 保持向下兼容的新增及修改时，递增次版本号；进行不向下兼容的修改时，递增主版本号。

我称这套系统为“语义化的版本控制”，在这套约定下，版本号及其更新方式包含了相邻版本间的底层代码和修改内容的信息。

[](#semver){.anchor-link}语义化版本控制规范（SemVer） {#semver}
-----------------------------------------------------

以下关键词 MUST、MUST NOT、REQUIRED、SHALL、SHALL NOT、SHOULD、SHOULD NOT、 RECOMMENDED、MAY、OPTIONAL 依照 RFC 2119 的叙述解读。（译注：为了保持语句顺畅， 以下文件遇到的关键词将依照整句语义进行翻译，在此先不进行个别翻译。）

1.  <div id="spec-item-1">

    </div>

    [](#spec-item-1){.anchor-link}

    使用语义化版本控制的软件“必须 MUST ”定义公共 API。该 API 可以在代码中被定义或出现于严谨的文件内。无论何种形式都应该力求精确且完整。

2.  <div id="spec-item-2">

    </div>

    [](#spec-item-2){.anchor-link}

    标准的版本号“必须 MUST ”采用 XYZ 的格式，其中 X、Y 和 Z 为非负的整数，且“禁止 MUST NOT”在数字前方补零。X 是主版本号、Y 是次版本号、而 Z 为修订号。每个元素“必须 MUST ”以数值来递增。例如：1.9.1 -&gt; 1.10.0 -&gt; 1.11.0。

3.  <div id="spec-item-3">

    </div>

    [](#spec-item-3){.anchor-link}

    标记版本号的软件发行后，“禁止 MUST NOT ”改变该版本软件的内容。任何修改都“必须 MUST ”以新版本发行。

4.  <div id="spec-item-4">

    </div>

    [](#spec-item-4){.anchor-link}

    主版本号为零（0.y.z）的软件处于开发初始阶段，一切都可能随时被改变。这样的公共 API 不应该被视为稳定版。

5.  <div id="spec-item-5">

    </div>

    [](#spec-item-5){.anchor-link}

    1.0.0 的版本号用于界定公共 API 的形成。这一版本之后所有的版本号更新都基于公共 API 及其修改内容。

6.  <div id="spec-item-6">

    </div>

    [](#spec-item-6){.anchor-link}

    修订号 Z（x.y.Z `|`{.highlighter-rouge} x &gt; 0）“必须 MUST ”在只做了向下兼容的修正时才递增。这里的修正指的是针对不正确结果而进行的内部修改。

7.  <div id="spec-item-7">

    </div>

    [](#spec-item-7){.anchor-link}

    次版本号 Y（x.Y.z `|`{.highlighter-rouge} x &gt; 0）“必须 MUST ”在有向下兼容的新功能出现时递增。在任何公共 API 的功能被标记为弃用时也“必须 MUST ”递增。也“可以 MAY ”在内部程序有大量新功能或改进被加入时递增，其中“可以 MAY ”包括修订级别的改变。每当次版本号递增时，修订号“必须 MUST ”归零。

8.  <div id="spec-item-8">

    </div>

    [](#spec-item-8){.anchor-link}

    主版本号 X（X.y.z `|`{.highlighter-rouge} X &gt; 0）“必须 MUST ”在有任何不兼容的修改被加入公共 API 时递增。其中“可以 MAY ”包括次版本号及修订级别的改变。每当主版本号递增时，次版本号和修订号“必须 MUST ”归零。

9.  <div id="spec-item-9">

    </div>

    [](#spec-item-9){.anchor-link}

    先行版本号“可以 MAY ”被标注在修订版之后，先加上一个连接号再加上一连串以句点分隔的标识符号来修饰。标识符号“必须 MUST ”由 ASCII 码的英数字和连接号 \[0-9A-Za-z-\] 组成，且“禁止 MUST NOT ”留白。数字型的标识符号“禁止 MUST NOT ”在前方补零。先行版的优先级低于相关联的标准版本。被标上先行版本号则表示这个版本并非稳定而且可能无法达到兼容的需求。范例：1.0.0-alpha、1.0.0-alpha.1、1.0.0-0.3.7、1.0.0-x.7.z.92。

10. <div id="spec-item-10">

    </div>

    [](#spec-item-10){.anchor-link}

    版本编译信息“可以 MAY ”被标注在修订版或先行版本号之后，先加上一个加号再加上一连串以句点分隔的标识符号来修饰。标识符号“必须 MUST ”由 ASCII 的英数字和连接号 \[0-9A-Za-z-\] 组成，且“禁止 MUST NOT ”留白。当判断版本的优先层级时，版本编译信息“可 SHOULD ”被忽略。因此当两个版本只有在版本编译信息有差别时，属于相同的优先层级。范例：1.0.0-alpha+001、1.0.0+20130313144700、1.0.0-beta+exp.sha.5114f85。

11. <div id="spec-item-11">

    </div>

    [](#spec-item-11){.anchor-link}

    版本的优先层级指的是不同版本在排序时如何比较。判断优先层级时，“必须 MUST ”把版本依序拆分为主版本号、次版本号、修订号及先行版本号后进行比较（版本编译信息不在这份比较的列表中）。由左到右依序比较每个标识符号，第一个差异值用来决定优先层级：主版本号、次版本号及修订号以数值比较，例如：1.0.0 &lt; 2.0.0 &lt; 2.1.0 &lt; 2.1.1。当主版本号、次版本号及修订号都相同时，改以优先层级比较低的先行版本号决定。例如：1.0.0-alpha &lt; 1.0.0。有相同主版本号、次版本号及修订号的两个先行版本号，其优先层级“必须 MUST ”透过由左到右的每个被句点分隔的标识符号来比较，直到找到一个差异值后决定：只有数字的标识符号以数值高低比较，有字母或连接号时则逐字以 ASCII 的排序来比较。数字的标识符号比非数字的标识符号优先层级低。若开头的标识符号都相同时，栏位比较多的先行版本号优先层级比较高。范例：1.0.0-alpha &lt; 1.0.0-alpha.1 &lt; 1.0.0-alpha.beta &lt; 1.0.0-beta &lt; 1.0.0-beta.2 &lt; 1.0.0-beta.11 &lt; 1.0.0- rc.1 &lt; 1.0.0。

[](#section-3){.anchor-link}为什么要使用语义化的版本控制？ {#section-3}
----------------------------------------------------------

这并不是一个新的或者革命性的想法。实际上，你可能已经在做一些近似的事情了。问题在于只是“近似”还不够。如果没有某个正式的规范可循，版本号对于依赖的管理并无实质意义。将上述的想法命名并给予清楚的定义，让你对软件使用者传达意向变得容易。一旦这些意向变得清楚，弹性（但又不会太弹性）的依赖规范就能达成。

举个简单的例子就可以展示语义化的版本控制如何让依赖地狱成为过去。假设有个名为“救火车”的函式库，它需要另一个名为“梯子”并已经有使用语义化版本控制的套件。当救火车创建时，梯子的版本号为 3.1.0。因为救火车使用了一些版本 3.1.0 所新增的功能， 你可以放心地指定相依于梯子的版本号大等于 3.1.0 但小于 4.0.0。这样，当梯子版本 3.1.1 和 3.2.0 发布时，你可以将直接它们纳入你的套件管理系统，因为它们能与原有相依的软件兼容。

作为一位负责任的开发者，你理当确保每次套件升级的运作与版本号的表述一致。现实世界是复杂的，我们除了提高警觉外能做的不多。你所能做的就是让语义化的版本控制为你提供一个健全的方式来发行以及升级套件，而无需推出新的相依套件，节省你的时间及烦恼。

如果你对此认同，希望立即开始使用语义化版本控制，你只需声明你的函式库正在使用它并遵循这些规则就可以了。请在你的 README 文件中保留此页连结，让别人也知道这些规则并从中受益。

[](#faq){.anchor-link}FAQ {#faq}
-------------------------

### [](#yz-){.anchor-link}在 0.y.z 初始开发阶段，我该如何进行版本控制？ {#yz-}

最简单的做法是以 0.1.0 作为你的初始化开发版本，并在后续的每次发行时递增次版本号。

### [](#section-4){.anchor-link}如何判断发布 1.0.0 版本的时机？ {#section-4}

当你的软件被用于正式环境，它应该已经达到了 1.0.0 版。如果你已经有个稳定的 API 被使用者依赖，也会是 1.0.0 版。如果你很担心向下兼容的问题，也应该算是 1.0.0 版了。

### [](#section-5){.anchor-link}这不会阻碍快速开发和迭代吗？ {#section-5}

主版本号为零的时候就是为了做快速开发。如果你每天都在改变 API，那么你应该仍在主版本号为零的阶段（0.y.z），或是正在下个主版本的独立开发分支中。

### [](#api-4200-){.anchor-link}对于公共 API，若即使是最小但不向下兼容的改变都需要产生新的主版本号，岂不是很快就达到 42.0.0 版？ {#api-4200-}

这是开发的责任感和前瞻性的问题。不兼容的改变不应该轻易被加入到有许多依赖代码的软件中。升级所付出的代价可能是巨大的。要递增主版本号来发行不兼容的改版，意味着你必须为这些改变所带来的影响深思熟虑，并且评估所涉及的成本及效益比。

### [](#api-){.anchor-link}为整个公共 API 写文件太费事了！ {#api-}

为供他人使用的软件编写适当的文件，是你作为一名专业开发者应尽的职责。保持专案高效一个非常重要的部份是掌控软件的复杂度，如果没有人知道如何使用你的软件或不知道哪些函数的调用是可靠的，要掌控复杂度会是困难的。长远来看，使用语义化版本控制以及对于公共 API 有良好规范的坚持，可以让每个人及每件事都运行顺畅。

### [](#section-6){.anchor-link}万一不小心把一个不兼容的改版当成了次版本号发行了该怎么办？ {#section-6}

一旦发现自己破坏了语义化版本控制的规范，就要修正这个问题，并发行一个新的次版本号来更正这个问题并且恢复向下兼容。即使是这种情况，也不能去修改已发行的版本。可以的话，将有问题的版本号记录到文件中，告诉使用者问题所在，让他们能够意识到这是有问题的版本。

### [](#api--1){.anchor-link}如果我更新了自己的依赖但没有改变公共 API 该怎么办？ {#api--1}

由于没有影响到公共 API，这可以被认定是兼容的。若某个软件和你的套件有共同依赖，则它会有自己的依赖规范，作者也会告知可能的冲突。要判断改版是属于修订等级或是次版等级，是依据你更新的依赖关系是为了修复问题或是加入新功能。对于后者，我经常会预期伴随着更多的代码，这显然会是一个次版本号级别的递增。

### [](#api--2){.anchor-link}如果我变更了公共 API 但无意中未遵循版本号的改动怎么办呢？（意即在修订等级的发布中，误将重大且不兼容的改变加到代码之中） {#api--2}

自行做最佳的判断。如果你有庞大的使用者群在依照公共 API 的意图而变更行为后会大受影响，那么最好做一次主版本的发布，即使严格来说这个修复仅是修订等级的发布。记住， 语义化的版本控制就是透过版本号的改变来传达意义。若这些改变对你的使用者是重要的，那就透过版本号来向他们说明。

### [](#section-7){.anchor-link}我该如何处理即将弃用的功能？ {#section-7}

弃用现存的功能是软件开发中的家常便饭，也通常是向前发展所必须的。当你弃用部份公共 API 时，你应该做两件事：（1）更新你的文件让使用者知道这个改变，（2）在适当的时机将弃用的功能透过新的次版本号发布。在新的主版本完全移除弃用功能前，至少要有一个次版本包含这个弃用信息，这样使用者才能平顺地转移到新版 API。

### [](#section-8){.anchor-link}语义化版本对于版本的字串长度是否有限制呢？ {#section-8}

没有，请自行做适当的判断。举例来说，长到 255 个字元的版本已过度夸张。再者，特定的系统对于字串长度可能会有他们自己的限制。

[](#section-9){.anchor-link}关于 {#section-9}
--------------------------------

语义化版本控制的规范是由 Gravatars 创办者兼 GitHub 共同创办者 [Tom Preston-Werner](http://tom.preston-werner.com) 所建立。

如果您有任何建议，请到 [GitHub 上提出您的问题](https://github.com/mojombo/semver/issues)。

[](#section-10){.anchor-link}授权 {#section-10}
---------------------------------

创用 CC 姓名标示 3.0 Unported 授权条款 http://creativecommons.org/licenses/by/3.0/

[](#semantic-versioning-200){.anchor-link}Semantic Versioning 2.0.0 {#semantic-versioning-200}
===================================================================

[](#summary){.anchor-link}Summary {#summary}
---------------------------------

Given a version number MAJOR.MINOR.PATCH, increment the:

1.  MAJOR version when you make incompatible API changes,
2.  MINOR version when you add functionality in a backwards-compatible manner, and
3.  PATCH version when you make backwards-compatible bug fixes.

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

[](#introduction){.anchor-link}Introduction {#introduction}
-------------------------------------------

In the world of software management there exists a dread place called “dependency hell.” The bigger your system grows and the more packages you integrate into your software, the more likely you are to find yourself, one day, in this pit of despair.

In systems with many dependencies, releasing new package versions can quickly become a nightmare. If the dependency specifications are too tight, you are in danger of version lock (the inability to upgrade a package without having to release new versions of every dependent package). If dependencies are specified too loosely, you will inevitably be bitten by version promiscuity (assuming compatibility with more future versions than is reasonable). Dependency hell is where you are when version lock and/or version promiscuity prevent you from easily and safely moving your project forward.

As a solution to this problem, I propose a simple set of rules and requirements that dictate how version numbers are assigned and incremented. These rules are based on but not necessarily limited to pre-existing widespread common practices in use in both closed and open-source software. For this system to work, you first need to declare a public API. This may consist of documentation or be enforced by the code itself. Regardless, it is important that this API be clear and precise. Once you identify your public API, you communicate changes to it with specific increments to your version number. Consider a version format of X.Y.Z (Major.Minor.Patch). Bug fixes not affecting the API increment the patch version, backwards compatible API additions/changes increment the minor version, and backwards incompatible API changes increment the major version.

I call this system “Semantic Versioning.” Under this scheme, version numbers and the way they change convey meaning about the underlying code and what has been modified from one version to the next.

[](#semantic-versioning-specification-semver){.anchor-link}Semantic Versioning Specification (SemVer) {#semantic-versioning-specification-semver}
-----------------------------------------------------------------------------------------------------

The key words “MUST”, “MUST NOT”, “REQUIRED”, “SHALL”, “SHALL NOT”, “SHOULD”, “SHOULD NOT”, “RECOMMENDED”, “MAY”, and “OPTIONAL” in this document are to be interpreted as described in [RFC 2119](http://tools.ietf.org/html/rfc2119).

1.  <div id="spec-item-1">

    </div>

    [](#spec-item-1){.anchor-link}

    Software using Semantic Versioning MUST declare a public API. This API could be declared in the code itself or exist strictly in documentation. However it is done, it should be precise and comprehensive.

2.  <div id="spec-item-2">

    </div>

    [](#spec-item-2){.anchor-link}

    A normal version number MUST take the form X.Y.Z where X, Y, and Z are non-negative integers, and MUST NOT contain leading zeroes. X is the major version, Y is the minor version, and Z is the patch version. Each element MUST increase numerically. For instance: 1.9.0 -&gt; 1.10.0 -&gt; 1.11.0.

3.  <div id="spec-item-3">

    </div>

    [](#spec-item-3){.anchor-link}

    Once a versioned package has been released, the contents of that version MUST NOT be modified. Any modifications MUST be released as a new version.

4.  <div id="spec-item-4">

    </div>

    [](#spec-item-4){.anchor-link}

    Major version zero (0.y.z) is for initial development. Anything may change at any time. The public API should not be considered stable.

5.  <div id="spec-item-5">

    </div>

    [](#spec-item-5){.anchor-link}

    Version 1.0.0 defines the public API. The way in which the version number is incremented after this release is dependent on this public API and how it changes.

6.  <div id="spec-item-6">

    </div>

    [](#spec-item-6){.anchor-link}

    Patch version Z (x.y.Z | x &gt; 0) MUST be incremented if only backwards compatible bug fixes are introduced. A bug fix is defined as an internal change that fixes incorrect behavior.

7.  <div id="spec-item-7">

    </div>

    [](#spec-item-7){.anchor-link}

    Minor version Y (x.Y.z | x &gt; 0) MUST be incremented if new, backwards compatible functionality is introduced to the public API. It MUST be incremented if any public API functionality is marked as deprecated. It MAY be incremented if substantial new functionality or improvements are introduced within the private code. It MAY include patch level changes. Patch version MUST be reset to 0 when minor version is incremented.

8.  <div id="spec-item-8">

    </div>

    [](#spec-item-8){.anchor-link}

    Major version X (X.y.z | X &gt; 0) MUST be incremented if any backwards incompatible changes are introduced to the public API. It MAY include minor and patch level changes. Patch and minor version MUST be reset to 0 when major version is incremented.

9.  <div id="spec-item-9">

    </div>

    [](#spec-item-9){.anchor-link}

    A pre-release version MAY be denoted by appending a hyphen and a series of dot separated identifiers immediately following the patch version. Identifiers MUST comprise only ASCII alphanumerics and hyphen \[0-9A-Za-z-\]. Identifiers MUST NOT be empty. Numeric identifiers MUST NOT include leading zeroes. Pre-release versions have a lower precedence than the associated normal version. A pre-release version indicates that the version is unstable and might not satisfy the intended compatibility requirements as denoted by its associated normal version. Examples: 1.0.0-alpha, 1.0.0-alpha.1, 1.0.0-0.3.7, 1.0.0-x.7.z.92.

10. <div id="spec-item-10">

    </div>

    [](#spec-item-10){.anchor-link}

    Build metadata MAY be denoted by appending a plus sign and a series of dot separated identifiers immediately following the patch or pre-release version. Identifiers MUST comprise only ASCII alphanumerics and hyphen \[0-9A-Za-z-\]. Identifiers MUST NOT be empty. Build metadata SHOULD be ignored when determining version precedence. Thus two versions that differ only in the build metadata, have the same precedence. Examples: 1.0.0-alpha+001, 1.0.0+20130313144700, 1.0.0-beta+exp.sha.5114f85.

11. <div id="spec-item-11">

    </div>

    [](#spec-item-11){.anchor-link}

    Precedence refers to how versions are compared to each other when ordered. Precedence MUST be calculated by separating the version into major, minor, patch and pre-release identifiers in that order (Build metadata does not figure into precedence). Precedence is determined by the first difference when comparing each of these identifiers from left to right as follows: Major, minor, and patch versions are always compared numerically. Example: 1.0.0 &lt; 2.0.0 &lt; 2.1.0 &lt; 2.1.1. When major, minor, and patch are equal, a pre-release version has lower precedence than a normal version. Example: 1.0.0-alpha &lt; 1.0.0. Precedence for two pre-release versions with the same major, minor, and patch version MUST be determined by comparing each dot separated identifier from left to right until a difference is found as follows: identifiers consisting of only digits are compared numerically and identifiers with letters or hyphens are compared lexically in ASCII sort order. Numeric identifiers always have lower precedence than non-numeric identifiers. A larger set of pre-release fields has a higher precedence than a smaller set, if all of the preceding identifiers are equal. Example: 1.0.0-alpha &lt; 1.0.0-alpha.1 &lt; 1.0.0-alpha.beta &lt; 1.0.0-beta &lt; 1.0.0-beta.2 &lt; 1.0.0-beta.11 &lt; 1.0.0-rc.1 &lt; 1.0.0.

[](#why-use-semantic-versioning){.anchor-link}Why Use Semantic Versioning? {#why-use-semantic-versioning}
--------------------------------------------------------------------------

This is not a new or revolutionary idea. In fact, you probably do something close to this already. The problem is that “close” isn’t good enough. Without compliance to some sort of formal specification, version numbers are essentially useless for dependency management. By giving a name and clear definition to the above ideas, it becomes easy to communicate your intentions to the users of your software. Once these intentions are clear, flexible (but not too flexible) dependency specifications can finally be made.

A simple example will demonstrate how Semantic Versioning can make dependency hell a thing of the past. Consider a library called “Firetruck.” It requires a Semantically Versioned package named “Ladder.” At the time that Firetruck is created, Ladder is at version 3.1.0. Since Firetruck uses some functionality that was first introduced in 3.1.0, you can safely specify the Ladder dependency as greater than or equal to 3.1.0 but less than 4.0.0. Now, when Ladder version 3.1.1 and 3.2.0 become available, you can release them to your package management system and know that they will be compatible with existing dependent software.

As a responsible developer you will, of course, want to verify that any package upgrades function as advertised. The real world is a messy place; there’s nothing we can do about that but be vigilant. What you can do is let Semantic Versioning provide you with a sane way to release and upgrade packages without having to roll new versions of dependent packages, saving you time and hassle.

If all of this sounds desirable, all you need to do to start using Semantic Versioning is to declare that you are doing so and then follow the rules. Link to this website from your README so others know the rules and can benefit from them.

[](#faq){.anchor-link}FAQ {#faq}
-------------------------

### [](#how-should-i-deal-with-revisions-in-the-0yz-initial-development-phase){.anchor-link}How should I deal with revisions in the 0.y.z initial development phase? {#how-should-i-deal-with-revisions-in-the-0yz-initial-development-phase}

The simplest thing to do is start your initial development release at 0.1.0 and then increment the minor version for each subsequent release.

### [](#how-do-i-know-when-to-release-100){.anchor-link}How do I know when to release 1.0.0? {#how-do-i-know-when-to-release-100}

If your software is being used in production, it should probably already be 1.0.0. If you have a stable API on which users have come to depend, you should be 1.0.0. If you’re worrying a lot about backwards compatibility, you should probably already be 1.0.0.

### [](#doesnt-this-discourage-rapid-development-and-fast-iteration){.anchor-link}Doesn’t this discourage rapid development and fast iteration? {#doesnt-this-discourage-rapid-development-and-fast-iteration}

Major version zero is all about rapid development. If you’re changing the API every day you should either still be in version 0.y.z or on a separate development branch working on the next major version.

### [](#if-even-the-tiniest-backwards-incompatible-changes-to-the-public-api-require-a-major-version-bump-wont-i-end-up-at-version-4200-very-rapidly){.anchor-link}If even the tiniest backwards incompatible changes to the public API require a major version bump, won’t I end up at version 42.0.0 very rapidly? {#if-even-the-tiniest-backwards-incompatible-changes-to-the-public-api-require-a-major-version-bump-wont-i-end-up-at-version-4200-very-rapidly}

This is a question of responsible development and foresight. Incompatible changes should not be introduced lightly to software that has a lot of dependent code. The cost that must be incurred to upgrade can be significant. Having to bump major versions to release incompatible changes means you’ll think through the impact of your changes, and evaluate the cost/benefit ratio involved.

### [](#documenting-the-entire-public-api-is-too-much-work){.anchor-link}Documenting the entire public API is too much work! {#documenting-the-entire-public-api-is-too-much-work}

It is your responsibility as a professional developer to properly document software that is intended for use by others. Managing software complexity is a hugely important part of keeping a project efficient, and that’s hard to do if nobody knows how to use your software, or what methods are safe to call. In the long run, Semantic Versioning, and the insistence on a well defined public API can keep everyone and everything running smoothly.

### [](#what-do-i-do-if-i-accidentally-release-a-backwards-incompatible-change-as-a-minor-version){.anchor-link}What do I do if I accidentally release a backwards incompatible change as a minor version? {#what-do-i-do-if-i-accidentally-release-a-backwards-incompatible-change-as-a-minor-version}

As soon as you realize that you’ve broken the Semantic Versioning spec, fix the problem and release a new minor version that corrects the problem and restores backwards compatibility. Even under this circumstance, it is unacceptable to modify versioned releases. If it’s appropriate, document the offending version and inform your users of the problem so that they are aware of the offending version.

### [](#what-should-i-do-if-i-update-my-own-dependencies-without-changing-the-public-api){.anchor-link}What should I do if I update my own dependencies without changing the public API? {#what-should-i-do-if-i-update-my-own-dependencies-without-changing-the-public-api}

That would be considered compatible since it does not affect the public API. Software that explicitly depends on the same dependencies as your package should have their own dependency specifications and the author will notice any conflicts. Determining whether the change is a patch level or minor level modification depends on whether you updated your dependencies in order to fix a bug or introduce new functionality. I would usually expect additional code for the latter instance, in which case it’s obviously a minor level increment.

### [](#what-if-i-inadvertently-alter-the-public-api-in-a-way-that-is-not-compliant-with-the-version-number-change-ie-the-code-incorrectly-introduces-a-major-breaking-change-in-a-patch-release){.anchor-link}What if I inadvertently alter the public API in a way that is not compliant with the version number change (i.e. the code incorrectly introduces a major breaking change in a patch release) {#what-if-i-inadvertently-alter-the-public-api-in-a-way-that-is-not-compliant-with-the-version-number-change-ie-the-code-incorrectly-introduces-a-major-breaking-change-in-a-patch-release}

Use your best judgment. If you have a huge audience that will be drastically impacted by changing the behavior back to what the public API intended, then it may be best to perform a major version release, even though the fix could strictly be considered a patch release. Remember, Semantic Versioning is all about conveying meaning by how the version number changes. If these changes are important to your users, use the version number to inform them.

### [](#how-should-i-handle-deprecating-functionality){.anchor-link}How should I handle deprecating functionality? {#how-should-i-handle-deprecating-functionality}

Deprecating existing functionality is a normal part of software development and is often required to make forward progress. When you deprecate part of your public API, you should do two things: (1) update your documentation to let users know about the change, (2) issue a new minor release with the deprecation in place. Before you completely remove the functionality in a new major release there should be at least one minor release that contains the deprecation so that users can smoothly transition to the new API.

### [](#does-semver-have-a-size-limit-on-the-version-string){.anchor-link}Does semver have a size limit on the version string? {#does-semver-have-a-size-limit-on-the-version-string}

No, but use good judgment. A 255 character version string is probably overkill, for example. Also, specific systems may impose their own limits on the size of the string.

[](#about){.anchor-link}About {#about}
-----------------------------

The Semantic Versioning specification is authored by [Tom Preston-Werner](http://tom.preston-werner.com), inventor of Gravatars and cofounder of GitHub.

If you’d like to leave feedback, please [open an issue on GitHub](https://github.com/mojombo/semver/issues).

[](#license){.anchor-link}License {#license}
---------------------------------

[Creative Commons - CC BY 3.0](http://creativecommons.org/licenses/by/3.0/)
