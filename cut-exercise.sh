# ANNMARIE AIDOO - NIC 300 LINUX ADMINSTRATION / ENTERPRISE SCRIPTING
# Read Chapter 4 of Learning the Bash Shell and complete the cut exercise along with the  pushd and popd exercise.  
# When and where would the pushed and popped function be useful?  
# When and where would the cut exercise be useful?
# Upload your code to github and submit the link.
# ======================================

# Send a mail message to everyone who is currently logged in.

mail $(who | cut -d' ' -f1)