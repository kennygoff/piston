import jinja2
import os
import shutil

template_loader = jinja2.FileSystemLoader(searchpath=os.getcwd())
template_env = jinja2.Environment(loader=template_loader)

if not os.path.exists("./build"):
    os.makedirs("./build")

for root, dirs, files in os.walk("."):
    if len(filter(root.startswith, ["./.git", "./build", "./venv"])):
        continue

    build_root = root[:1] + "/build" + root[1:]
    if not os.path.exists(build_root):
        os.makedirs(build_root)

    for filebase in files:
        if filebase.startswith("."):
            continue

        filename, fileext = os.path.splitext(filebase)
        fileroot = "%s/%s" % (root, filebase)
        filebuild = "%s/%s" % (build_root, filebase)

        if fileext == ".jinja":
            template = template_env.get_template(fileroot)
            template_vars = {
                "relroot": "../" * (build_root.count("/") - 1)
            }
            output = template.render(template_vars)

            filebuild = "%s/%s.html" % (build_root, filename)
            with open(filebuild, "wb") as fh:
                fh.write(output)
        else:
            shutil.copy(fileroot, filebuild)
