#/usr/bin/env python
from string import Template
# Creates configs, and cvs file to produce requests.
# Produce requests with:
#   python manageRequests.py --clone SMP-RunIISummer15GS-00113 cloneSherpaZZ4Lrequest.csv
zggpoints = [
    "0p002I0p00002",
    "0p002I0p0",
    "0p002Im0p00002",
    "0p0I0p00002",
    "0p0I0p0",
    "0p0Im0p00002",
    "m0p002I0p00002",
    "m0p002I0p0",
    "m0p002Im0p00002",
]
def makePoint(x):
    x = x.replace("p", ".")
    x = x.replace("m", "-")
    if x == "0": x = "0.0"
    return x
def getChecksum(point):
    file_name = "/afs/cern.ch/user/k/kelong/work/MCContactTests/SherpaZvvgamma/Cards/aTGC-Zgg/sherpa_%s_MASTER_cff_py_GEN.py" % point
    lines = open(file_name).readlines()
    check_line = ""
    for line in lines:
        if "Checksum" in line:
            check_line = line
            break
    return check_line.split("'")[1]
config = Template("".join(open("SherpaConfigs/Zvvg_aTGC-Zgg_template").readlines()))
vals = {
    "process" : "0I0",
    "h3g" : "0",
    "h4g" : "0",
    "checksum" : "0",
}
csv_file_name = "clone_SherpaZvvg_atgcZgg_request.csv"
with open(csv_file_name, "w") as csv_file:
    csv_file.write("prepid,Dataset name,path to fragment\n")
for i,point in enumerate(zggpoints):
    vals["process"] = point
    h3g,h4g = point.split("I")
    vals["h3g"] = makePoint(h3g)
    vals["h4g"] = makePoint(h4g)
    vals["checksum"] = getChecksum(point)
    name = "ZGTo2NuG_aTGC-Zgg_h3-%s_h4-%s_13TeV-sherpa" % (h3g, h4g)

    fragment_name = "SherpaConfigs/Zvvg_aTGC-Zgg/%s_fragment.py" % name
    with open(fragment_name, "w") as out_config:
        out_config.write(config.substitute(vals))
    with open(csv_file_name, "a") as csv_file:
        csv_file.write(",".join(["SMP-RunIISummer15GS-001%i" % (56+i), name, fragment_name]) +"\n")
