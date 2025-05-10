import psutil
import json
import sys


class ProcessInfo:
    def __init__(self, pid, name, exe, cmdline, status):
        self.pid = pid
        self.name = name
        self.exe = exe
        self.cmdline = cmdline
        self.status = status
        self.children = []

    def to_dict(self):
        return {
            "pid": self.pid,
            "name": self.name,
            "exe": self.exe,
            "cmdline": self.cmdline,
            "status": self.status,
            "children": [child.to_dict() for child in self.children]
        }

    def add_child(self, child):
        self.children.append(child)


class ProcessTree:
    def __init__(self):
        self.all_procs = {}
        self.pid_tree = {}

    def get_process_info(self, proc):
        try:
            return ProcessInfo(
                proc.pid,
                proc.name(),
                proc.exe(),
                proc.cmdline(),
                proc.status()
            )
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess) as e:
            print(f"[!] Skipping PID {proc.pid}: {type(e).__name__} - {e}", file=sys.stderr)
            return None

    def build_process_tree(self):
        # Barcha protsesslarni yig'ish
        for proc in psutil.process_iter():
            info = self.get_process_info(proc)
            if info:
                self.all_procs[proc.pid] = info
                ppid = proc.ppid()
                self.pid_tree.setdefault(ppid, []).append(proc.pid)

        visited = set()

        def attach_children(proc_info):
            visited.add(proc_info.pid)
            pid = proc_info.pid
            children_pids = self.pid_tree.get(pid, [])
            for child_pid in children_pids:
                child_info = self.all_procs.get(child_pid)
                if child_info and child_pid not in visited:
                    proc_info.add_child(attach_children(child_info))
            return proc_info

        all_processes = []

        for pid, proc_info in self.all_procs.items():
            if pid not in visited:
                all_processes.append(attach_children(proc_info))

        return all_processes

    def save_to_json(self, filename="process_tree.json"):
        tree = self.build_process_tree()
        with open(filename, "w", encoding="utf-8") as f:
            json.dump([process.to_dict() for process in tree], f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    print("[*] Gathering process tree...")
    process_tree = ProcessTree()
    process_tree.save_to_json()
    print("[+] Saved to process_tree.json")
