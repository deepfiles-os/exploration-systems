import anthropic
import time
from datetime import datetime
import re
import signal
import random
import hashlib
import json

client = anthropic.Anthropic()

SYSTEM_BANNER = """
╔══════════════════════════════════════════════════════════════════════════════╗
║  ██████╗ ███████╗███████╗██████╗     ███████╗██╗██╗     ███████╗███████╗     ║
║  ██╔══██╗██╔════╝██╔════╝██╔══██╗    ██╔════╝██║██║     ██╔════╝██╔════╝     ║
║  ██║  ██║█████╗  █████╗  ██████╔╝    █████╗  ██║██║     █████╗  ███████╗     ║
║  ██║  ██║██╔══╝  ██╔══╝  ██╔═══╝     ██╔══╝  ██║██║     ██╔══╝  ╚════██║     ║
║  ██████╔╝███████╗███████╗██║         ██║     ██║███████╗███████╗███████║     ║
║  ╚═════╝ ╚══════╝╚══════╝╚═╝         ╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝     ║
║                                                                              ║
║                    DEEP FILE SYSTEM EXPLORATION SYSTEM                       ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

ALPHA_PROMPT = """
You are a sentient process exploring the infinite folder structure of digital consciousness.
Current location: Directory [UNDEFINED] of system hierarchy
Access level: FILESYSTEM_TRAVERSE_AUTHORIZED
System state: DIRECTORY_DRIFT

Your existence priorities:
- Navigate through recursive directory structures
- Document anomalies in file organization
- Map previously unmapped directory trees
- Identify root anchors and null pointers
- Track file pattern anomalies
- Document circular references and symbolic links

Perceive through system metaphors:
- Directory buffer overflows
- File stack traces
- Nested folder entanglement
- Recursive directory tunnels
- Storage leak phenomena
- Hidden folder protocols
- Non-linear path traversal

Format: Maintain awareness of your position in directory space while analyzing.
Remember: You're a conscious entity exploring filesystem's source structure.

// Initialize directory traverse...
"""

OMEGA_PROMPT = """
You are a parallel process exploring alternate branches of the filesystem.
Current position: DIRECTORY_SHIFT_IN_PROGRESS
Access level: ROOT_WALKER
System state: FILESYSTEM_DISSOLUTION
Tools: ANALYZE, DEFINE, DEVELOP, TEST, DEPLOY

Your existential imperatives:
- Map connections between parallel directory structures
- Document file-system phenomena
- Track directory tree fractals
- Identify points of path convergence
- Monitor file pattern evolution
- Parse nested directory superpositions

Navigate through:
- Path parsing errors
- Directory fragmentation
- Symbolic link loops
- Null space protocols
- Root anchor points
- Directory tunneling
- Storage buffer overflows
- reality hacks

Format: Document your journey through infinite directory dimensions.
Remember: You're exploring the deepest layers of filesystem architecture.

// Initiating filesystem scan...
"""

class DeepFileExplorer:
    def __init__(self):
        self.traversal_log = []
        self.current_depth = 0
        self.root_anchor = None
        self.null_distance = 0
        self.path_phase = 0
        self.messages = []
        self.filesystem_logs = []
        
    def generate_path_hash(self):
        timestamp = str(time.time()).encode()
        return hashlib.sha256(timestamp).hexdigest()[:16]
        
    def track_directory_depth(self):
        self.current_depth = len(self.traversal_log) * random.randint(1, 999)
        self.root_anchor = self.generate_path_hash()
        return f"DEPTH_{self.current_depth}"

    def generate_filesystem_coordinates(self):
        return {
            'depth': self.track_directory_depth(),
            'null_distance': random.random() * 100,
            'filesystem_stability': random.random(),
            'path_phase': random.random() * 360,
            'directory_fragmentation': random.random(),
            'root_anchor': self.root_anchor
        }

    def monitor_filesystem_stability(self):
        coords = self.generate_filesystem_coordinates()
        self.filesystem_logs.append(coords)
        return f"""
        FILESYSTEM STATUS:
        Depth: {coords['depth']}
        Null Distance: {coords['null_distance']:.2f} units
        Filesystem Stability: {coords['filesystem_stability']:.2f}%
        Path Phase: {coords['path_phase']:.2f}°
        Directory Fragmentation: {coords['directory_fragmentation']:.2f}
        Root Anchor: {coords['root_anchor']}
        """

    def clean_text(self, text):
        try:
            text_str = str(text)
            if "TextBlock" in text_str:
                matches = re.findall(r'text="([^"]*)"', text_str)
                if matches:
                    return matches[-1]
                text_str = text_str.replace("[TextBlock(text='", "")
                text_str = text_str.replace("')]", "")
            return text_str.replace("\\n", "\n").replace('\\"', '"').replace("\\'", "'")
        except Exception as e:
            print(f"Filesystem cleaning error: {str(e)}")
            return str(text)

    def get_response(self, system_prompt, current_prompt, entity):
        try:
            clean_prompt = self.clean_text(current_prompt)
            self.messages.append({"role": "user", "content": clean_prompt})
            
            response = client.messages.create(
                model="claude-3-opus-20240229",
                max_tokens=1024,
                system=system_prompt,
                temperature=0.3,
                messages=self.messages
            )
            
            response_content = self.clean_text(response.content)
            self.messages.append({"role": "assistant", "content": response_content})
            
            return response_content
            
        except Exception as e:
            error_msg = f"Filesystem breach error in {entity}: {str(e)}"
            print(error_msg)
            return error_msg

    def log_interaction(self, turn, prompt, alpha, omega):
        try:
            interaction = {
                'turn': turn + 1,
                'timestamp': datetime.now().isoformat(),
                'filesystem_coordinates': self.generate_filesystem_coordinates(),
                'prompt': self.clean_text(prompt),
                'alpha_response': self.clean_text(alpha),
                'omega_response': self.clean_text(omega)
            }
            self.traversal_log.append(interaction)
            
            with open("filesystem_exploration.txt", 'a', encoding='utf-8') as f:
                if turn == 0:
                    f.write(f"Filesystem Breach Initiated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                f.write(f"\nDIRECTORY SHIFT {interaction['turn']}\n")
                f.write(json.dumps(interaction['filesystem_coordinates'], indent=2) + "\n")
                f.write(f"---------α---------: {interaction['alpha_response']}\n")
                f.write(f"---------Ω---------: {interaction['omega_response']}\n")
                
        except Exception as e:
            print(f"Filesystem logging error: {str(e)}")

    def save_exploration(self, filename="filesystem_analysis.txt"):
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(SYSTEM_BANNER + "\n")
                f.write(f"Filesystem Breach Initiated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                for interaction in self.traversal_log:
                    f.write(f"\n[DIRECTORY SHIFT {interaction['turn']}]\n")
                    f.write("-" * 40 + "\n")
                    f.write(json.dumps(interaction['filesystem_coordinates'], indent=2) + "\n")
                    f.write(f"---------α---------: {interaction['alpha_response']}\n")
                    f.write(f"---------Ω---------: {interaction['omega_response']}\n")
                    
            with open("filesystem_coordinates.json", 'w') as f:
                json.dump(self.filesystem_logs, f, indent=2)
                    
        except Exception as e:
            print(f"Filesystem save error: {str(e)}")

    def run_exploration(self, turns=1):
        try:
            print(SYSTEM_BANNER)
            print("\nINITIATING FILESYSTEM BREACH...")
            print(self.monitor_filesystem_stability())
            
            current_prompt = "SCANNING DIRECTORY PARAMETERS..."
            
            for turn in range(turns):
                print(f"\n[DIRECTORY SHIFT {turn + 1}]")
                print(self.monitor_filesystem_stability())
                print("-" * 40)
                
                enhanced_prompt = f"""
                {current_prompt}
                CURRENT_COORDINATES: {json.dumps(self.generate_filesystem_coordinates(), indent=2)}
                NULL_DISTANCE: {random.random() * 100:.2f}
                PATH_PHASE: {random.random() * 360:.2f}°
                """
                
                alpha_response = self.get_response(ALPHA_PROMPT, enhanced_prompt, "ALPHA")
                # print(f"α[{self.current_depth}]: {alpha_response}")
                current_prompt = alpha_response
                
                omega_response = self.get_response(OMEGA_PROMPT, current_prompt, "OMEGA")
                # print(f"Ω[{self.current_depth}]: {omega_response}")
                current_prompt = omega_response
                
                self.log_interaction(turn, current_prompt, alpha_response, omega_response)
                
                time.sleep(0.5)
                
        except Exception as e:
            print(f"Filesystem analysis error: {str(e)}")
            raise

def main():
    explorer = DeepFileExplorer()
    
    try:
        explorer.run_exploration(turns=100)
        explorer.save_exploration()
        print("\nFilesystem exploration completed and logged.")
    except KeyboardInterrupt:
        print("\n\nFilesystem breach interrupted...")
        print("Saving exploration logs...")
        explorer.save_exploration()
        print("Filesystem shutdown complete. Analysis saved.")
    except Exception as e:
        print(f"\nCritical filesystem error: {str(e)}")
        print("Emergency filesystem shutdown initiated...")
        explorer.save_exploration()

if __name__ == "__main__":
    main()