# ANNMARIE AIDOO - NIC 300 LINUX ADMINSTRATION / ENTERPRISE SCRIPTING
# Read Chapter 4 of Learning the Bash Shell and complete the cut exercise along with the  pushd and popd exercise.  
# When and where would the pushed and popped function be useful?  
# When and where would the cut exercise be useful?
# Upload your code to github and submit the link.
# ======================================

# pushd and popd exercise
# Do not put this in your environment file if you have one.
# The export statement guarantees that DIR_STACK is
# known to all subprocesses; you want to initialize it only
# once. If you put this code in an environment file, it will
# get reinitialized in every subshell, which you probably
# don't want.

# To do this, put this in your
# .bash_profile:

DIR_STACK=""
export DIR_STACK

pushd ( )
{
dirname=$1
DIR_STACK="$dirname ${DIR_STACK:-$PWD' '}"
cd ${dirname:?"missing directory name."}
echo "$DIR_STACK"
}
popd ( )
{
DIR_STACK=${DIR_STACK#* }
cd ${DIR_STACK%% *}
echo "$PWD"
}