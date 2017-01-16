#/usr/bin/env python
from string import Template
# Creates configs, and cvs file to produce requests.
# Produce requests with:
#   python manageRequests.py --clone SMP-RunIISummer15GS-00113 cloneSherpaZZ4Lrequest.csv
##0I0p003
##0I0p0015
##0I0
##0Im0p003
##0Im0p0015
##0p0019I0p0015
##0p0019I0
##0p0019Im0p0015
#0p0019I0p003
##    "0p0038I0",
##    "0p0019Im0p003",
f5points = [
    "0p0038I0p0015",
    "0p0038I0p003",
    "0p0038Im0p0015",
    "0p0038Im0p003",
    "m0p0019I0",
    "m0p0019I0p0015",
    "m0p0019I0p003",
    "m0p0019Im0p0015",
    "m0p0019Im0p003",
    "m0p0038I0p0015",
    "m0p0038I0",
    "m0p0038I0p003",
    "m0p0038Im0p0015",
    "m0p0038Im0p003",
]
def makePoint(x):
    x = x.replace("p", ".")
    x = x.replace("m", "-")
    if x == "0": x = "0.0"
    return x
def getChecksum(point):
    file_name = "/afs/cern.ch/user/k/kelong/work/MCContactTests/SherpaZZTo4L/Cards/sherpa_%s_MASTER_cff_py_GEN_SIM.py" % point
    lines = open(file_name).readlines()
    check_line = ""
    for line in lines:
        if "Checksum" in line:
            check_line = line
            break
    return check_line.split("'")[1]
config = Template("".join(open("SherpaConfigs/ZZ4L_template").readlines()))
vals = {
    "process" : "0I0",
    "f5z" : "0",
    "f5g" : "0",
    "checksum" : "0",
}
csv_file_name = "cloneSherpaZZ4Lrequest.csv"
with open(csv_file_name, "w") as csv_file:
    csv_file.write("prepid,Dataset name,path to fragment\n")
for i,point in enumerate(f5points):
    vals["process"] = point
    f5z,f5g = point.split("I")
    vals["f5z"] = makePoint(f5z)
    vals["f5g"] = makePoint(f5g)
    vals["checksum"] = getChecksum(point)
    name = "ZZTo4L_aTGC-f5_fg-%s_fz-%s_13TeV-sherpa" % (f5z, f5g)

    fragment_name = "SherpaConfigs/%s_fragment.py" % name
    with open(fragment_name, "w") as out_config:
        out_config.write(config.substitute(vals))
    with open("clone_SherpaZZ4L_atgcf5_request.csv", "a") as csv_file:
        csv_file.write(",".join(["SMP-RunIISummer15GS-0011%i" % (5+i), name, fragment_name]) +"\n")
