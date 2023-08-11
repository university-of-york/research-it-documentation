Beginners Guide to the Linux Shell
==================================

Intro
-----

The shell has been the major interface for the Unix/Linux operating system since it was first conceived. The shell allows interaction with the operating system through a text based interface. The shell provides the user with the following features:

    - An easy to use command line interface (CLI)
    - Combine existing tools to create new tools
    - Input/output redirection
    - Wildcard characters for filename abbreviation
    - Variables and options for environment customisation
    - Ability to write shell functions and programs
    - Command-line editing
    - Command history (quick access to previous commands)
    - Arithmetic
    - Command abreviations

The user starts the shell by logging into the computer with a userid and password:

.. code-block:: console
    :caption: logging in

    ******************************************************************************
    ***                   THE UNIVERSITY OF YORK IT SERVICES                   ***
    ***                                                                        ***
    ***                       THIS IS A PRIVATE COMPUTER                       ***
    ***                UNAUTHORISED ACCESS STRICTLY PROHIBITED                 ***
    ******************************************************************************

    login: user001
    password:
    Last login: Mon Sep  8 14:12:44 2014 from gallifrey.york.ac.uk
    -bash-4.1$

The last line is a ``command prompt`` and it is the means by which the computer is telling you that it is ready to accept a command from you. If you do not see the prompt, the computer is probability still executing the last command you have typed. The user types commands which take the form:

:command:`command [ options ] [ arguments ]`

Options to a command are usually proceeded by a ``-`` or ``--``, this differentiates them from the arguments. The following example shows the ``echo`` command which prints the arguments and the ``ls`` command which take options arguments. The ``ls`` command display the users file. There will be more explanation of files and the ``ls`` command later.

.. code-block:: console
    :caption: example of command execution

    -bash-4.1$ echo Hello World
    Hello World
    -bash-4.1$ ls
    bin  Chemistry  Desktop  examples  Experiments  intel  jobs  logs  tmp
    -bash-4.1$ ls -l
    total 296
    drwxr-xr-x 2 abs4 csrv        4096 Jun 24 09:39 bin
    drwxr-xr-x 3 abs4 csrv        4096 Jun  6 09:23 Chemistry
    drwxr-sr-x 2 abs4 elecclust   4096 Mar 11 10:53 Desktop
    drwxr-xr-x 3 abs4 csrv        4096 Jun 30 12:21 examples
    drwxr-xr-x 5 abs4 csrv        4096 May 23 11:34 Experiments
    drwxr-xr-x 3 abs4 csrv        4096 Aug 14 12:26 intel
    drwxr-sr-x 3 abs4 elecclust   4096 Aug 15 12:49 jobs
    drwxr-xr-x 2 abs4 csrv      266240 Aug 15 13:48 logs
    drwxr-xr-x 3 abs4 csrv        4096 Aug 14 14:50 tmp
    -bash-4.1$

To logout of the shell type ``logout``, ``exit`` or press ``Ctrl + D``.

.. code-block:: console
    :caption: logging out

    -bash-4.1$ exit
    logout
    Connection to ecgberht closed.

.. note::

    The are a number of shells available to the user. In this tutorial we will be using `Bash <https://www.gnu.org/software/bash/>`_, the most widely used Linux shell.


Files and Directories
---------------------

Filesystem Organisation
^^^^^^^^^^^^^^^^^^^^^^^

The file system is the component of the operating system that organises data into files. These files are organised into directories.

When you have logged in you will be placed in a directory which is called your ``home`` directory. To find the name of the directory use the ``pwd`` command (print working directory). Use the ``cd`` command to change directory.

.. code-block:: console
    :caption: locating your home directory and files

    -bash-4.1$ pwd
    /usr/researchcomp/elecclust/abs4
    -bash-4.1$ cd /usr
    -bash-4.1$ pwd
    /usr
    -bash-4.1$ cd
    -bash-4.1$ pwd
    /usr/researchcomp/elecclust/abs4
    -bash-4.1$ cd ..
    -bash-4.1$ pwd
    /usr/researchcomp/elecclust
    -bash-4.1$ cd .
    -bash-4.1$ pwd
    /usr/researchcomp/elecclust
    -bash-4.1$

The output of the ``pwd`` command, ``/usr/researchcomp/elecclust/abs4``, is called a *pathname*, and this specifies the location of the users home directory. The first ``/`` in the pathname is the *root directory*. Names following the ``/`` are directory names. Directories within directories are called sub-directories. Pathanmes can also specify the location within the filesystem of files. Only the last name of a pathaname can be a file or directory.

The ``cd`` command lets you change your working directory to another location in the file system. ``cd`` with no arguments places you back in your home directory. The special directory ``..`` references the directory above your current directory (known as the parent directory). The is another special direcory ``.`` which references the current directory. These two directories can be viewed as *links*.


Listing Files and Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

To list the files in a directory use the ``ls`` (list) command.

.. code-block:: console

    -bash-4.1$ ls
    afile  bin  Chemistry  Desktop  examples  Experiments  intel  jobs  logs  tmp
    -bash-4.1$ ls -l
    total 296
    -rw-r--r-- 1 abs4 csrv           0 Sep  8 16:26 afile
    drwxr-xr-x 2 abs4 csrv        4096 Jun 24 09:39 bin
    drwxr-xr-x 3 abs4 csrv        4096 Jun  6 09:23 Chemistry
    drwxr-sr-x 2 abs4 elecclust   4096 Mar 11 10:53 Desktop
    drwxr-xr-x 3 abs4 csrv        4096 Jun 30 12:21 examples
    drwxr-xr-x 5 abs4 csrv        4096 May 23 11:34 Experiments
    drwxr-xr-x 3 abs4 csrv        4096 Aug 14 12:26 intel
    drwxr-sr-x 3 abs4 elecclust   4096 Aug 15 12:49 jobs
    drwxr-xr-x 2 abs4 csrv      266240 Aug 15 13:48 logs
    drwxr-xr-x 3 abs4 csrv        4096 Aug 14 14:50 tmp


``ls`` without any options or arguments lists the names of the files and directories in the current working directory. In this example above it can be hard to see which names refer to files or directories. We will show you how to do this later on.

The ``-a`` option shows *all* files, filenames starting with ``.`` are usually hidden from display.

.. code-block:: console

    -bash-4.1$ ls -a
    .              Experiments      intel             .profile
    ..             .felix           jobs              .pulse
    afile          .gconf           .lesshst          .pulse-cookie
    .bash_history  .gconfd          .local            .python_history
    bin            .gnome2          logs              .qmon_preferences
    Chemistry      .gnote           .matlab           .Rhistory
    .config        .gnupg           .mcrCache8.3      .ssh
    .dbus          .gstreamer-0.10  .modulerc         .subversion
    Desktop        .gvfs            .nautilus         tmp
    .emacs.d       .history         .ngspice_history  .Xauthority
    examples       .ICEauthority    .nx


We can combine options to give more detail.

.. code-block:: console

    -bash-4.1$ ls -al
    total 440
    drwx------ 30 abs4   elecclust   4096 Sep  8 16:26 .
    drwxrws--- 14 jaw500 elecclust   4096 Sep  8 16:25 ..
    -rw-r--r--  1 abs4   csrv           0 Sep  8 16:26 afile
    -rw-------  1 abs4   elecclust  16495 Sep  8 15:40 .bash_history
    drwxr-xr-x  2 abs4   csrv        4096 Jun 24 09:39 bin
    drwxr-xr-x  3 abs4   csrv        4096 Jun  6 09:23 Chemistry
    drwxr-sr-x  4 abs4   elecclust   4096 Mar 11 10:53 .config
    drwx--S---  3 abs4   elecclust   4096 Mar 11 10:51 .dbus
    drwxr-sr-x  2 abs4   elecclust   4096 Mar 11 10:53 Desktop
    drwxr-xr-x  3 abs4   csrv        4096 May 23 14:52 .emacs.d
    drwxr-xr-x  3 abs4   csrv        4096 Jun 30 12:21 examples
    drwxr-xr-x  5 abs4   csrv        4096 May 23 11:34 Experiments
    drwxr-xr-x  2 abs4   csrv        4096 Jul  1 12:00 .felix
    drwx--S---  4 abs4   elecclust   4096 May  2 16:09 .gconf
    drwx--S---  2 abs4   elecclust   4096 May  2 16:34 .gconfd
    drwx--S---  4 abs4   elecclust   4096 Mar 11 10:53 .gnome2
    drwxr-sr-x  3 abs4   elecclust   4096 Mar 11 10:53 .gnote
    drwx--S---  2 abs4   elecclust   4096 Mar 11 10:52 .gnupg
    drwxr-sr-x  2 abs4   elecclust   4096 Mar 11 10:53 .gstreamer-0.10
    drwx--S---  2 abs4   elecclust   4096 Mar 11 10:52 .gvfs
    -rw-------  1 abs4   csrv         978 Jun  6 09:32 .history
    -rw-------  1 abs4   elecclust    314 Mar 11 10:52 .ICEauthority
    drwxr-xr-x  3 abs4   csrv        4096 Aug 14 12:26 intel
    drwxr-sr-x  3 abs4   elecclust   4096 Aug 15 12:49 jobs
    -rw-------  1 abs4   csrv          46 Jun  6 09:31 .lesshst
    drwxr-sr-x  3 abs4   elecclust   4096 Mar 11 10:52 .local
    drwxr-xr-x  2 abs4   csrv      266240 Aug 15 13:48 logs
    drwxr-xr-x  3 abs4   csrv        4096 May  2 16:06 .matlab
    drwxr-xr-x  9 abs4   csrv        4096 Jul  3 11:54 .mcrCache8.3
    -rw-r--r--  1 abs4   csrv          32 Sep  5 08:05 .modulerc
    drwxr-sr-x  2 abs4   elecclust   4096 Mar 11 10:53 .nautilus
    -rw-------  1 abs4   elecclust      0 Jan 13  2014 .ngspice_history
    drwx--S---  6 abs4   elecclust   4096 Apr 25 13:36 .nx
    -rw-r--r--  1 abs4   elecclust    145 May 19 11:59 .profile
    drwx------  2 abs4   csrv        4096 Mar 11 10:54 .pulse
    -rw-------  1 abs4   elecclust    256 Mar 11 10:54 .pulse-cookie
    -rw-------  1 abs4   csrv          49 Jun  3 13:42 .python_history
    -rw-r--r--  1 abs4   csrv         342 Jun 16 12:57 .qmon_preferences
    -rw-------  1 abs4   csrv          40 May 23 11:09 .Rhistory
    drwxr-sr-x  2 abs4   elecclust   4096 Jun  5 12:53 .ssh
    drwxr-xr-x  2 abs4   csrv        4096 May  2 16:06 .subversion
    drwxr-xr-x  3 abs4   csrv        4096 Aug 14 14:50 tmp
    -rw-------  1 abs4   csrv         488 Sep  8 15:48 .Xauthority
    -bash-4.1$

The next example displays the directory in the long format using the ``-l`` option, much more information is displayed about the directories and files.
``ls`` can take arguments as well. When specifying an argument ``ls`` displays the information for *that* file or directory.

.. code-block:: console

    -bash-4.1$ ls Experiments
    architest.dtr                   OLD               simple_verbs.dtr~
    architest.dtr~                  OLD CART          simple verbs_to_Dunstan.txt
    exploded.csv                    ordered           simple verbs_to_Dunstan.xlsx
    Latest CART                     phon.csv          simple_verbs_to.txt
    mian.rp                         phonsorted        simple_verbs.txt
    NotesAboutInfixPredictions.pdf  simple_verbs.dtr  simpverbsort
    -bash-4.1$ ls -l Experiments
    total 368
    -rw-r--r-- 1 abs4 csrv    919 May 23 11:08 architest.dtr
    -rw-r--r-- 1 abs4 csrv    909 May 23 11:08 architest.dtr~
    -rw-r--r-- 1 abs4 csrv   3613 May 23 11:08 exploded.csv
    drwxr-xr-x 2 abs4 csrv   4096 May 23 11:34 Latest CART
    -rw-r--r-- 1 abs4 csrv   4019 May 23 11:28 mian.rp
    -rw-r--r-- 1 abs4 csrv 193602 May 23 11:08 NotesAboutInfixPredictions.pdf
    drwxr-xr-x 2 abs4 csrv   4096 May 23 11:08 OLD
    drwxr-xr-x 2 abs4 csrv   4096 May 23 11:08 OLD CART
    -rw-r--r-- 1 abs4 csrv   3613 May 23 11:08 ordered
    -rw-r--r-- 1 abs4 csrv   6217 May 23 11:08 phon.csv
    -rw-r--r-- 1 abs4 csrv   6217 May 23 11:08 phonsorted
    -rw-r--r-- 1 abs4 csrv  17663 May 23 11:08 simple_verbs.dtr
    -rw-r--r-- 1 abs4 csrv  17647 May 23 11:08 simple_verbs.dtr~
    -rw-r--r-- 1 abs4 csrv   8058 May 23 11:08 simple verbs_to_Dunstan.txt
    -rw-r--r-- 1 abs4 csrv  30416 May 23 11:08 simple verbs_to_Dunstan.xlsx
    -rw-r--r-- 1 abs4 csrv   4696 May 23 11:08 simple_verbs_to.txt
    -rw-r--r-- 1 abs4 csrv  17525 May 23 11:08 simple_verbs.txt
    -rw-r--r-- 1 abs4 csrv  17647 May 23 11:08 simpverbsort
    -bash-4.1$ ls -ld Experiments
    drwxr-xr-x 5 abs4 csrv 4096 May 23 11:34 Experiments
    -bash-4.1$ ls -l afile
    -rw-r--r-- 1 abs4 csrv 0 Sep  8 16:26 afile
    -bash-4.1$ ls /usr
    appl          cmsmigratetest  lfa       phpweb        src       vleexam
    archive       cvs             lib       puppet        systems   vle-sysadmin
    backups       datasets        lib64     puppetdev     tmp       webmisc
    bin           etc             libexec   researchcomp  transfer  work
    central       games           local     rlink         userfs    yorkroot
    cert          idm             logfiles  sbin          UserFS    yorkweb
    cmsmedia      include         mirror    scratch       vle       yorkwebtest
    cmsmediatest  java            misc      secbuffer     vle-arch
    cmsmigrate    kerberos        opapp     share         vle-eldt
    -bash-4.1$

Using a directory name as an option causes ``ls`` to list the contents of the directory. To list the attributes of the directory use the ``-d`` option. You can use a pathname as the argument.


Creating, Moving and Copying Files and Directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can create directories, move or copy files or directories to other locations in the filesystem using the ``mkdir`` (make directory) ``mv`` (move) and ``cp`` (copy) commands.

.. code-block:: console
    :caption: create a new directory

    -bash-4.1$ ls
    afile  bin        Desktop   Experiments  jobs  new-dir
    bfile  Chemistry  examples  intel        logs  tmp
    -bash-4.1$ mv afile new-dir
    -bash-4.1$ cp bfile new-dir
    -bash-4.1$ ls
    bfile  Chemistry  examples     intel  logs     tmp
    bin    Desktop    Experiments  jobs   new-dir
    -bash-4.1$ ls new-dir
    afile  bfile
    -bash-4.1$ mv new-dir/afile .
    -bash-4.1$ ls
    afile  bin        Desktop   Experiments  jobs  new-dir
    bfile  Chemistry  examples  intel        logs  tmp
    -bash-4.1$

This example creates a new directory, ``new-dir``, We then move the file ``afile`` to it and create a copy of ``bfile``. We then move the file ``afile`` back to our current working directory. Note the use of the ``.`` file to reference the current working directory. We can use full or partial pathnames to reference other parts of the file system.

Copying a directory is a little more complicated and the directory may contain files and directories. We use the ``-r`` command to cp to do this.

.. code-block:: console
    :caption: copying a directory

    -bash-4.1$ ls
    afile  bin        Desktop   Experiments  jobs  tmp
    bfile  Chemistry  examples  intel        logs
    -bash-4.1$ ls tmp
    icc-start  ifort-start  logs       mpi-stop  start  test
    icc-stop   ifort-stop   mpi-start  new-dir   stop
    -bash-4.1$ cp tmp/test .
    cp: omitting directory `tmp/test'
    -bash-4.1$ cp -r tmp/test .
    -bash-4.1$ ls
    afile  bin        Desktop   Experiments  jobs  test
    bfile  Chemistry  examples  intel        logs  tmp
    -bash-4.1$ ls test
    test.c  test.cpp  test.f  test.f90  test.x
    -bash-4.1$

In this example we wish to copy the contents of the directory ``tmp/test`` into the current directory. ``cp`` will not copy a directory by default. We have to use the ``-r`` (recursive) option to tell ``cp`` to copy all files and directories within the directory.


Deleting files and directories
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``rm`` (remove) command is used to delete files.

.. code-block::
    :caption: Deleting files and directories

    -bash-4.1$ ls
    afile  bin        Desktop   Experiments  jobs  test
    bfile  Chemistry  examples  intel        logs  tmp
    -bash-4.1$ rm bfile
    -bash-4.1$ ls
    afile  Chemistry  examples     intel  logs  tmp
    bin    Desktop    Experiments  jobs   test
    -bash-4.1$

To delete directories use the ``rmdir`` (remove directory) command.

.. code-block:: console
    :caption: Deleting directories and their contents

    -bash-4.1$ rmdir dira
    rmdir: failed to remove `dira': Directory not empty
    -bash-4.1$ rm -r dira
    -bash-4.1$ ls
    afile  Chemistry  dirb      Experiments  jobs  test
    bin    Desktop    examples  intel        logs  tmp
    -bash-4.1$ rm -ri dirb
    rm: descend into directory `dirb'? y
    rm: descend into directory `dirb/dirb'? y
    rm: remove regular empty file `dirb/dirb/afile'? y
    rm: remove directory `dirb/dirb'? y
    rm: remove regular empty file `dirb/afile'? y
    rm: remove directory `dirb'? y
    -bash-4.1$

``rmdir`` will only remove empty directories. To remove a directory and all it's contents use the ``rm -r`` (recursive) option to the ``rm`` command. To be safe and check the files before you remove them use ``rm -ri`` (recursive and interactive) options.


Editing and Displaying the Contents of Files
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Text Editors
""""""""""""

  - vi and vim
  - emacs
  - nano

Displaying the contents of files
""""""""""""""""""""""""""""""""

The commands ``cat`` (concatenate files) and more displays the contents of file.

.. code-block:: console
    :caption: ``cat`` and ``more``

    -bash-4.1$ cat snark2

    The Hunting of the Snark
    By Lewis Carroll
    Fit the First
                The Landing

    "Just the place for a Snark!" the Bellman cried,
       As he landed his crew with care;
    Supporting each man on the top of the tide
       By a finger entwined in his hair.

    "Just the place for a Snark! I have said it twice:
       That alone should encourage the crew.
    Just the place for a Snark! I have said it thrice:
       What I tell you three times is true."

    -bash-4.1$ more snark
    The Hunting of the Snark
    By Lewis Carroll
                Fit the First
                The Landing
    "Just the place for a Snark!" the Bellman cried,
       As he landed his crew with care;
    Supporting each man on the top of the tide
       By a finger entwined in his hair.
    "Just the place for a Snark! I have said it twice:
       That alone should encourage the crew.
    Just the place for a Snark! I have said it thrice:
       What I tell you three times is true."
    The crew was complete: it included a Boots—
       A maker of Bonnets and Hoods—
    A Barrister, brought to arrange their disputes—
       And a Broker, to value their goods.
    A Billiard-marker, whose skill was immense,
    --More--(2%)


The ``cat`` command displays all the text in the users file on the screen. This can prove difficult to read if there are large amounts of text. The ``more`` command paginates the text and displays portions of it on the screen. The user can use character command to move through the file:

   | ``SPACE``       - display the next screen of text
   | ``q``           - quit displaying the file
   | ``b``           - skip backwards through he file
   | ``/pattern``    - search for text in the file


Files and Directory Permissions
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Groups are provided to manage sets of users and control access to files and directories. All users belong to a default group and may be a member of other groups.

.. code-block:: console
    :caption: group membership

    -bash-4.1$ groups
    csrv pfs17 pfs34 csys cvssys itsilg rhpcs sshfix git5 git6 git7 elecclust yc-gauss yc-install yc-colum
    -bash-4.1$ ls -l
    total 332
    -rw-r--r-- 1 abs4 csrv           0 Sep  8 16:26 afile
    drwxr-xr-x 2 abs4 csrv        4096 Jun 24 09:39 bin
    drwxr-xr-x 3 abs4 csrv        4096 Jun  6 09:23 Chemistry
    drwxr-sr-x 2 abs4 elecclust   4096 Mar 11 10:53 Desktop
    drwxr-xr-x 3 abs4 csrv        4096 Jun 30 12:21 examples
    drwxr-xr-x 5 abs4 csrv        4096 May 23 11:34 Experiments
    drwxr-xr-x 3 abs4 csrv        4096 Aug 14 12:26 intel
    drwxr-sr-x 3 abs4 elecclust   4096 Aug 15 12:49 jobs
    drwxr-xr-x 2 abs4 csrv      266240 Aug 15 13:48 logs
    -rw-r--r-- 1 abs4 csrv       25678 Sep  9 10:24 snark
    -rw-r--r-- 1 abs4 csrv         433 Sep  9 10:27 snark2
    drwxr-xr-x 2 abs4 csrv        4096 Sep  8 17:08 test
    drwxr-x--- 5 abs4 csrv        4096 Sep  8 17:01 tmp
    -bash-4.1$


The ``groups`` command displays which groups you are a member of. Each file and directory you create will be owned by you and be potentially accessible to a group. In the above example the file ``afile`` is owned by ``abs4`` and is accessible to the ``csrv`` group.

There is a ``special`` group sometimes called ``world``, or ``other``,  which contains all users of the system.

In the above example the first column of the directory listing shows the permissions of the files. These permissions control who is allowed access the files and directories. There are three categories of user who can have potential rights to access the files - ``owner``, ``group``, ``world``. The access rights to the files are displayed in the form of a sequence of letters like ``drwxr-xr-x``. The meaning is:

.. code-block:: console

    directory
    |
    drwxr-xr-x
     |_||_||_|
      |  |  |
      |  |  other permissions
      |  group permissions
      user permissions

    d - if present, this is a directory, otherwise it is a file. The following three
        letters are in three groups and state the access permissions for the owner,
        group, world users
    w - the file can be written to
    r - the file can be read
    x - if a file: it can be executed, if a directory: it can be accessed

.. code-block:: console
    :caption: example

    drwxr-x--- 5 abs4 csrv        4096 Sep  8 17:01 tmp

This is a ``directory``, the owner ``abs4`` can ``read``, ``write`` and ``access`` the directory. Members of the group, ``csrv``, can ``read`` and ``access`` the directory, they can not create or ``write`` to files in the directory, all ``other`` users do not have any access to the directory.


Chaning Permissions
""""""""""""""""""""

To change file permissions use the ``chmod`` command.

.. code-block:: console

    -bash-4.1$ ls -l snark
    -rw-r--r-- 1 abs4 csrv 25678 Sep  9 10:24 snark
    -bash-4.1$ chmod go-rwx snark
    -bash-4.1$ ls -l snark
    -rw------- 1 abs4 csrv 25678 Sep  9 10:24 snark

The chmod command has the form:

.. code-block:: console

    chmod <mode> <file>

    mode takes the form of:

    [ugoa...][[+-=][perms...]...]

    u = user (owner)
    g = group
    o = other (world)
    a = all (user, group, other)

    + add permission
    - remove permission
    = explicitly set permission

    w = can be written to
    r = can be read
    x = can be executed if a file, if a directory it can be accessed

.. code-block:: console
    :caption: some examples


    -bash-4.1$ ls -l snark
    -rw-r--r-- 1 abs4 csrv 25678 Sep  9 10:24 snark
    -bash-4.1$ chmod a+rx snark
    -bash-4.1$ ls -l snark
    -rwxr-xr-x 1 abs4 csrv 25678 Sep  9 10:24 snark
    -bash-4.1$ chmod go-rwx snark
    -bash-4.1$ ls -l snark
    -rwx------ 1 abs4 csrv 25678 Sep  9 10:24 snark
    -bash-4.1$ chmod u-w snark
    -bash-4.1$ ls -l snark
    -r-x------ 1 abs4 csrv 25678 Sep  9 10:24 snark
    -bash-4.1$ chmod a=r snark
    -bash-4.1$ ls -l snark
    -r--r--r-- 1 abs4 csrv 25678 Sep  9 10:24 snark
    -bash-4.1$ chmod u=w snark
    -bash-4.1$ ls -l snark
    --w-r--r-- 1 abs4 csrv 25678 Sep  9 10:24 snark
    -bash-4.1$ chmod u+r snark
    -bash-4.1$ ls -l snark
    -rw-r--r-- 1 abs4 csrv 25678 Sep  9 10:24 snark
    -bash-4.1$

To change the group of a file use the  command ``chgrp <groupname> <filename>``.

.. code-block:: console
    :caption: changing group of a file

    -bash-4.1$ ls -l snark
    -rw-r--r-- 1 abs4 csrv 25678 Sep  9 10:24 snark
    -bash-4.1$ groups
    csrv pfs17 pfs34 csys cvssys itsilg rhpcs sshfix git5 git6 git7 elecclust yc-gauss yc-install yc-colum
    -bash-4.1$ chgrp rhpcs snark
    -bash-4.1$ ls -l snark
    -rw-r--r-- 1 abs4 rhpcs 25678 Sep  9 10:24 snark
    -bash-4.1$


History, Command Line Editing and Job Control
---------------------------------------------

History
^^^^^^^

The history command lists the last commands you typed.

.. code-block:: console
    :caption: command history

    -bash-4.1$ history
    1  cd
    2  ls -l
    3  who
    4  ps
    5  sleep 200 &
    6  ps
    7  fg
    8  history
    -bash-4.1$


Command Line Editing
^^^^^^^^^^^^^^^^^^^^

You can select past commands using the up and down arrow keys. You can edit the command line using the left and right arrow keys and any of the following commands:

===============     =====================================
Keystroke           Result
===============     =====================================
Ctrl-P	            previous command
Ctrl-N	            next command
Ctrl-R *string*	    previous command containing *string*
Ctrl-B	            move back one character
Ctrl-F	            move forward one character
DEL	                delete previous character
Ctrl-D	            delete character under cursor
ESC-D	            delete word forward
ESC-H	            delete word backward
Ctrl-T	            transpose two characters
ESC-F	            move forward one word
ESC-B	            move back one word
===============     =====================================


Job Control
^^^^^^^^^^^

Job control deals with managing your programs whilst they are running. Linux uses the name process for a running program. The ``ps`` command list all the processes you have running.

.. code-block:: console
    :caption: listing your running processes

    -bash-4.1$ ps
      PID TTY          TIME CMD
    14521 pts/3    00:00:00 bash
    16165 pts/3    00:00:00 ps
    -bash-4.1$


From this we can see that we have two processes running, the ``bash`` shell and the ``ps`` command. Associated with each process is a unique identifier - ``PID`` (process ID).

We can manage processes, especially commands that take a long time to run, by making them a ``background process`` adding an ``&`` to the end of the line. The shell then becomes free for us to execute more commands.

.. code-block:: console
    :caption: management of background processes

    -bash-4.1$ ps
      PID TTY          TIME CMD
    14521 pts/3    00:00:00 bash
    17005 pts/3    00:00:00 ps
    -bash-4.1$ sleep 120
    ^C
    -bash-4.1$ sleep 120 &
    [1] 17026
    -bash-4.1$ ps
      PID TTY          TIME CMD
    14521 pts/3    00:00:00 bash
    17026 pts/3    00:00:00 sleep
    17027 pts/3    00:00:00 ps
    -bash-4.1$ echo I am doing other work
    I am doing other work
    -bash-4.1$ echo my work is complete
    my work is complete
    [1]+  Done                    sleep 120
    -bash-4.1$


The sleep command does nothing for the number of seconds specified in the argument. The first invocation of sleep is terminated (killed) by the impatient user typing ``Ctrl-c``. The second invocation places the command in the background, we are then able to do other work. The ``Done`` statement informs us that the command has terminated.

.. code-block:: console
    :caption: managing your background jobs

    -bash-4.1$ sleep 360 &
    [1] 17761
    -bash-4.1$ sleep 1000 &
    [2] 17766
    -bash-4.1$ jobs
    [1]-  Running                 sleep 360 &
    [2]+  Running                 sleep 1000 &
    -bash-4.1$ fg
    sleep 1000
    ^Z
    [2]+  Stopped                 sleep 1000
    -bash-4.1$ jobs
    [1]-  Running                 sleep 360 &
    [2]+  Stopped                 sleep 1000
    -bash-4.1$ bg
    [2]+ sleep 1000 &
    -bash-4.1$ jobs
    [1]-  Running                 sleep 360 &
    [2]+  Running                 sleep 1000 &
    x-bash-4.1$ fg %1
    sleep 360
    ^C
    -bash-4.1$ jobs
    [2]+  Running                 sleep 1000 &
    -bash-4.1$


In this example we put two jobs into the background. The ``fg`` command moves the last job placed in the background into the foreground. ``Ctrl-z`` stops (pauses, not kills) the job and returns to the command line. The ``bg`` command places the paused job in the background. ``fg`` can bring specific jobs to the foreground by specifying the job number.

Environment Variables and Shell Scripts
---------------------------------------

Environment Variables
^^^^^^^^^^^^^^^^^^^^^

In the Linux shell a variable is a named object that contains data and which can be used by programs and commands.  Environment variables provides a simple way to share configuration settings between multiple applications and processes in Linux. For example the value of an environmental variable can be the default editor that should be used, which can then be used by command to invoke the correct editor when necessary.


Predefined Environment Variables
""""""""""""""""""""""""""""""""
==========  =========================================================================
Variable    Value
==========  =========================================================================
HOME        path to the home directory of the current user.
PWD	        path to your working directory.
OLDPWD	    path to your previous working directory.
SHELL	    name of the running, interactive shell, e.g. ``bash``
TERM	    name of the running terminal, e.g. ``xterm``
PAGER	    path to the program used to list the contents of files, e.g. ``/bin/less``
EDITOR	    path to the program used for editing files, e.g. ``/usr/bin/nano``
==========  =========================================================================


To use an environment variable precede its name with a ``$`` character. We can display all define environment variables with ``printenv``, and set values with export.

.. code-block:: console
    :caption: using environment variables

    -bash-4.1$ echo $PWD
    /usr/researchcomp/elecclust/abs4
    -bash-4.1$ export MYVAR="My variable"
    -bash-4.1$ echo $MYVAR
    My variable
    -bash-4.1$ export MYVAR="My current directory is ${PWD}"
    -bash-4.1$ echo $MYVAR
    My current directory is /usr/researchcomp/elecclust/abs4
    -bash-4.1$


Shell Scripts
^^^^^^^^^^^^^

Shell scripts are files which contain shell commands. You run the script by typing its filename. Things to note:

    - The first line of the file should contain the string ``#!/bin/bash``. This informs the shell which program to run the script
    - Consider adding execute permission to the file to allow easy execution
    - Create a directory in your home directory to place all your scripts and add the directory path to your ``PATH`` variable

.. code-block:: console
    :caption: example

    -bash-4.1$ cat simple
    #!/bin/bash
    echo "I am a very simple script"

    -bash-4.1$ sh simple
    I am a very simple script
    -bash-4.1$ chmod u+x simple
    -bash-4.1$ ls -l simple
    -rwxr--r-- 1 abs4 csrv 46 Sep 11 12:28 simple
    -bash-4.1$ ./simple
    I am a very simple script
    -bash-4.1$ chmod u+x simple
    -bash-4.1$ ls -l simple
    -rwxr--r-- 1 abs4 csrv 46 Sep 11 12:28 simple
    -bash-4.1$ ./simple
    I am a very simple script
    -bash-4.1$ pwd
    /usr/researchcomp/elecclust/abs4/scripts
    -bash-4.1$ simple
    -bash: simple: command not found
    -bash-4.1$ export PATH="${PATH}:${HOME}/scripts"
    -bash-4.1$ simple
    I am a very simple script
    -bash-4.1$


Input and Output Redirection, Pipes, and Filters
------------------------------------------------

Input and Redirection
^^^^^^^^^^^^^^^^^^^^^

We can change the behaviour of programs to redirect input from a file instead of the keyboard and write to a file instead of the screen. The ``>`` character is used to redirect output to a file and ``<`` to redirect input.

.. code-block:: console
    :caption: Redirection of program I/O

    -bash-4.1$ echo Hello World > afile
    -bash-4.1$ cat afile
    Hello World
    -bash-4.1$ wc -l < wordsworth
    25
    -bash-4.1$

The ``wc -l`` command counts the number of lines typed. In this example we have redirected the input from a file.


Pipes
^^^^^^

Pipes allow the output of one program to be fed into the input of another. The ``|`` is the pipe symbol.

This example counts the number of lines in a set of files. We write the output to a file. The file is then sorted, using the sort command, into ascending order to give us the file order by number of lines.

.. code-block:: console
    :caption: count lines in a file

    -bash-4.1$ ls
    carroll  keats  milton  tennyson  thomas  wordsworth
    -bash-4.1$ wc -l * > linecount
    -bash-4.1$ cat linecount
      733 carroll
      423 keats
      156 milton
       11 tennyson
       28 thomas
       25 wordsworth
     1376 total
    -bash-4.1$ sort -n -k 1 linecount
       11 tennyson
       25 wordsworth
       28 thomas
      156 milton
      423 keats
      733 carroll
     1376 total
    -bash-4.1$

First we count the lines in each of the six file and redirect the output to a file. We then ``sort`` the file by the first column in numerical order.

A quicker and more efficient way without using the intermediary file is to use a pipe.



Useful Commands
---------------
