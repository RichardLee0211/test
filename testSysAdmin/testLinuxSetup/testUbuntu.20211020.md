#### fix the black screen after update issue from Ubuntu 18.04 to Ubuntu 20

dmesg

from: https://askubuntu.com/questions/162075/my-computer-boots-to-a-black-screen-what-options-do-i-have-to-fix-it/162078#162078

sudo apt remove --purge '^nvidia-.*'
sudo apt install ubuntu-desktop
sudo rm /et/cX11/xorg.confg
echo "inouveau" | sudo tee -a /etc/modules

this works, from: https://askubuntu.com/questions/1124057/ubuntu-18-04-stuck-at-purple-loading-screen-after-new-update
```shell
	sudo apt-get update
	sudo apt-get install --reinstall lightdm
	sudo dpkg-reconfigure lightdm
```

##### debug
```shell
(base) ╭─vislab at vislab-inwin in ~ 21-10-11 - 16:07:58
	╰─○ dmesg
	[    0.000000] microcode: microcode updated early to revision 0x28, date = 2019-11-12
	[    0.000000] Linux version 5.4.0-88-generic (buildd@lgw01-amd64-008) (gcc version 9.3.0 (Ubuntu 9.3.0-17ubuntu1~20.04)) #99-Ubuntu SMP Thu Sep 23 17:29:00 UTC 2021 (Ubuntu 5.4.0-88.99-generic 5.4.140)
	[    0.000000] Command line: BOOT_IMAGE=/boot/vmlinuz-5.4.0-88-generic root=UUID=1199f619-397d-4d1d-b2fb-512f97d76ee9 ro quiet splash vt.handoff=7
	[    0.000000] KERNEL supported cpus:
	[    0.000000]   Intel GenuineIntel
	[    0.000000]   AMD AuthenticAMD
	[    0.000000]   Hygon HygonGenuine
	[    0.000000]   Centaur CentaurHauls
	[    0.000000]   zhaoxin   Shanghai
	[    0.000000] x86/fpu: Supporting XSAVE feature 0x001: 'x87 floating point registers'
	[    0.000000] x86/fpu: Supporting XSAVE feature 0x002: 'SSE registers'
	[    0.000000] x86/fpu: Supporting XSAVE feature 0x004: 'AVX registers'
	[    0.000000] x86/fpu: xstate_offset[2]:  576, xstate_sizes[2]:  256
	[    0.000000] x86/fpu: Enabled xstate features 0x7, context size is 832 bytes, using 'standard' format.
	[    0.000000] BIOS-provided physical RAM map:
	[    0.000000] BIOS-e820: [mem 0x0000000000000000-0x000000000009d7ff] usable
	[    0.000000] BIOS-e820: [mem 0x000000000009d800-0x000000000009ffff] reserved
	[    0.000000] BIOS-e820: [mem 0x00000000000e0000-0x00000000000fffff] reserved
	[    0.000000] BIOS-e820: [mem 0x0000000000100000-0x00000000cac86fff] usable
	[    0.000000] BIOS-e820: [mem 0x00000000cac87000-0x00000000cac8dfff] ACPI NVS
	[    0.000000] BIOS-e820: [mem 0x00000000cac8e000-0x00000000cb0d1fff] usable
	[    0.000000] BIOS-e820: [mem 0x00000000cb0d2000-0x00000000cb662fff] reserved
	[    0.000000] BIOS-e820: [mem 0x00000000cb663000-0x00000000dd415fff] usable
	[    0.000000] BIOS-e820: [mem 0x00000000dd416000-0x00000000dd4b1fff] reserved
	[    0.000000] BIOS-e820: [mem 0x00000000dd4b2000-0x00000000dd502fff] usable
	[    0.000000] BIOS-e820: [mem 0x00000000dd503000-0x00000000dd63bfff] ACPI NVS
	[    0.000000] BIOS-e820: [mem 0x00000000dd63c000-0x00000000deffefff] reserved
	[    0.000000] BIOS-e820: [mem 0x00000000defff000-0x00000000deffffff] usable
	[    0.000000] BIOS-e820: [mem 0x00000000f8000000-0x00000000fbffffff] reserved
	[    0.000000] BIOS-e820: [mem 0x00000000fec00000-0x00000000fec00fff] reserved
	[    0.000000] BIOS-e820: [mem 0x00000000fed00000-0x00000000fed03fff] reserved
	[    0.000000] BIOS-e820: [mem 0x00000000fed1c000-0x00000000fed1ffff] reserved
	[    0.000000] BIOS-e820: [mem 0x00000000fee00000-0x00000000fee00fff] reserved
	[    0.000000] BIOS-e820: [mem 0x00000000ff000000-0x00000000ffffffff] reserved
	[    0.000000] BIOS-e820: [mem 0x0000000100000000-0x000000041effffff] usable
	[    0.000000] NX (Execute Disable) protection: active
	[    0.000000] SMBIOS 2.8 present.
	[    0.000000] DMI: MSI MS-7845/Z87-GD65 GAMING (MS-7845), BIOS V1.9 02/21/2014
	[    0.000000] tsc: Fast TSC calibration using PIT
	[    0.000000] tsc: Detected 3999.964 MHz processor
	[    0.001136] e820: update [mem 0x00000000-0x00000fff] usable ==> reserved
	[    0.001137] e820: remove [mem 0x000a0000-0x000fffff] usable
	[    0.001141] last_pfn = 0x41f000 max_arch_pfn = 0x400000000
	[    0.001144] MTRR default type: uncachable
	[    0.001145] MTRR fixed ranges enabled:
	[    0.001146]   00000-9FFFF write-back
	[    0.001146]   A0000-BFFFF uncachable
	[    0.001147]   C0000-CFFFF write-protect
	[    0.001147]   D0000-E7FFF uncachable
	[    0.001147]   E8000-FFFFF write-protect
	[    0.001148] MTRR variable ranges enabled:
	[    0.001149]   0 base 0000000000 mask 7C00000000 write-back
	[    0.001149]   1 base 0400000000 mask 7FF0000000 write-back
	[    0.001150]   2 base 0410000000 mask 7FF8000000 write-back
	[    0.001150]   3 base 0418000000 mask 7FFC000000 write-back
	[    0.001150]   4 base 041C000000 mask 7FFE000000 write-back
	[    0.001151]   5 base 041E000000 mask 7FFF000000 write-back
	[    0.001151]   6 base 00E0000000 mask 7FE0000000 uncachable
	[    0.001152]   7 disabled
	[    0.001152]   8 disabled
	[    0.001152]   9 disabled
	[    0.001399] x86/PAT: Configuration [0-7]: WB  WC  UC- UC  WB  WP  UC- WT
	[    0.001501] total RAM covered: 16368M
	[    0.001746] Found optimal setting for mtrr clean up
	[    0.001747]  gran_size: 64K  chunk_size: 32M         num_reg: 7      lose cover RAM: 0G
	[    0.001971] e820: update [mem 0xe0000000-0xffffffff] usable ==> reserved
	[    0.001974] last_pfn = 0xdf000 max_arch_pfn = 0x400000000
	[    0.006884] found SMP MP-table at [mem 0x000fd800-0x000fd80f]
	[    0.013236] check: Scanning 1 areas for low memory corruption
	[    0.013240] Using GB pages for direct mapping
	[    0.013603] RAMDISK: [mem 0x31ca5000-0x34e49fff]
	[    0.013606] ACPI: Early table checksum verification disabled
	[    0.013608] ACPI: RSDP 0x00000000000F04A0 000024 (v02 ALASKA)
	[    0.013610] ACPI: XSDT 0x00000000DD60B080 000084 (v01 ALASKA A M I    01072009 AMI  00010013)
	[    0.013614] ACPI: FACP 0x00000000DD61A148 00010C (v05 ALASKA A M I    01072009 AMI  00010013)
	[    0.013617] ACPI: DSDT 0x00000000DD60B1A0 00EFA5 (v02 ALASKA A M I    00000034 INTL 20120711)
	[    0.013619] ACPI: FACS 0x00000000DD63BF80 000040
	[    0.013620] ACPI: APIC 0x00000000DD61A258 000092 (v03 ALASKA A M I    01072009 AMI  00010013)
	[    0.013622] ACPI: FPDT 0x00000000DD61A2F0 000044 (v01 ALASKA A M I    01072009 AMI  00010013)
	[    0.013624] ACPI: ASF! 0x00000000DD61A338 0000A5 (v32 INTEL   HCG     00000001 TFSM 000F4240)
	[    0.013625] ACPI: SSDT 0x00000000DD61A3E0 000539 (v01 PmRef  Cpu0Ist  00003000 INTL 20120711)
	[    0.013627] ACPI: SSDT 0x00000000DD61A920 000AD8 (v01 PmRef  CpuPm    00003000 INTL 20120711)
	[    0.013629] ACPI: MCFG 0x00000000DD61B3F8 00003C (v01 ALASKA A M I    01072009 MSFT 00000097)
	[    0.013630] ACPI: HPET 0x00000000DD61B438 000038 (v01 ALASKA A M I    01072009 AMI. 00000005)
	[    0.013632] ACPI: SSDT 0x00000000DD61B470 00036D (v01 SataRe SataTabl 00001000 INTL 20120711)
	[    0.013633] ACPI: SSDT 0x00000000DD61B7E0 0034E1 (v01 SaSsdt SaSsdt   00003000 INTL 20091112)
	[    0.013635] ACPI: DMAR 0x00000000DD61ECC8 000080 (v01 INTEL  HSW      00000001 INTL 00000001)
	[    0.013637] ACPI: SSDT 0x00000000DD61ED48 000A26 (v01 Intel_ IsctTabl 00001000 INTL 20120711)
	[    0.013638] ACPI: Reserving FACP table memory at [mem 0xdd61a148-0xdd61a253]
	[    0.013639] ACPI: Reserving DSDT table memory at [mem 0xdd60b1a0-0xdd61a144]
	[    0.013639] ACPI: Reserving FACS table memory at [mem 0xdd63bf80-0xdd63bfbf]
	[    0.013640] ACPI: Reserving APIC table memory at [mem 0xdd61a258-0xdd61a2e9]
	[    0.013640] ACPI: Reserving FPDT table memory at [mem 0xdd61a2f0-0xdd61a333]
	[    0.013640] ACPI: Reserving ASF! table memory at [mem 0xdd61a338-0xdd61a3dc]
	[    0.013641] ACPI: Reserving SSDT table memory at [mem 0xdd61a3e0-0xdd61a918]
	[    0.013641] ACPI: Reserving SSDT table memory at [mem 0xdd61a920-0xdd61b3f7]
	[    0.013642] ACPI: Reserving MCFG table memory at [mem 0xdd61b3f8-0xdd61b433]
	[    0.013642] ACPI: Reserving HPET table memory at [mem 0xdd61b438-0xdd61b46f]
	[    0.013643] ACPI: Reserving SSDT table memory at [mem 0xdd61b470-0xdd61b7dc]
	[    0.013643] ACPI: Reserving SSDT table memory at [mem 0xdd61b7e0-0xdd61ecc0]
	[    0.013643] ACPI: Reserving DMAR table memory at [mem 0xdd61ecc8-0xdd61ed47]
	[    0.013644] ACPI: Reserving SSDT table memory at [mem 0xdd61ed48-0xdd61f76d]
	[    0.013650] ACPI: Local APIC address 0xfee00000
	[    0.013707] No NUMA configuration found
	[    0.013708] Faking a node at [mem 0x0000000000000000-0x000000041effffff]
	[    0.013715] NODE_DATA(0) allocated [mem 0x41efd5000-0x41effffff]
	[    0.013844] Zone ranges:
	[    0.013845]   DMA      [mem 0x0000000000001000-0x0000000000ffffff]
	[    0.013845]   DMA32    [mem 0x0000000001000000-0x00000000ffffffff]
	[    0.013846]   Normal   [mem 0x0000000100000000-0x000000041effffff]
	[    0.013846]   Device   empty
	[    0.013847] Movable zone start for each node
	[    0.013849] Early memory node ranges
	[    0.013849]   node   0: [mem 0x0000000000001000-0x000000000009cfff]
	[    0.013850]   node   0: [mem 0x0000000000100000-0x00000000cac86fff]
	[    0.013851]   node   0: [mem 0x00000000cac8e000-0x00000000cb0d1fff]
	[    0.013851]   node   0: [mem 0x00000000cb663000-0x00000000dd415fff]
	[    0.013851]   node   0: [mem 0x00000000dd4b2000-0x00000000dd502fff]
	[    0.013852]   node   0: [mem 0x00000000defff000-0x00000000deffffff]
	[    0.013852]   node   0: [mem 0x0000000100000000-0x000000041effffff]
	[    0.013962] Zeroed struct page in unavailable ranges: 16788 pages
	[    0.013962] Initmem setup node 0 [mem 0x0000000000001000-0x000000041effffff]
	[    0.013963] On node 0 totalpages: 4177516
	[    0.013964]   DMA zone: 64 pages used for memmap
	[    0.013964]   DMA zone: 21 pages reserved
	[    0.013965]   DMA zone: 3996 pages, LIFO batch:0
	[    0.013996]   DMA32 zone: 14076 pages used for memmap
	[    0.013997]   DMA32 zone: 900816 pages, LIFO batch:63
	[    0.021408]   Normal zone: 51136 pages used for memmap
	[    0.021409]   Normal zone: 3272704 pages, LIFO batch:63
	[    0.046863] ACPI: PM-Timer IO Port: 0x1808
	[    0.046866] ACPI: Local APIC address 0xfee00000
	[    0.046871] ACPI: LAPIC_NMI (acpi_id[0xff] high edge lint[0x1])
	[    0.046880] IOAPIC[0]: apic_id 8, version 32, address 0xfec00000, GSI 0-23
	[    0.046881] ACPI: INT_SRC_OVR (bus 0 bus_irq 0 global_irq 2 dfl dfl)
	[    0.046882] ACPI: INT_SRC_OVR (bus 0 bus_irq 9 global_irq 9 high level)
	[    0.046883] ACPI: IRQ0 used by override.
	[    0.046883] ACPI: IRQ9 used by override.
	[    0.046884] Using ACPI (MADT) for SMP configuration information
	[    0.046885] ACPI: HPET id: 0x8086a701 base: 0xfed00000
	[    0.046888] TSC deadline timer available
	[    0.046888] smpboot: Allowing 8 CPUs, 0 hotplug CPUs
	[    0.046901] PM: Registered nosave memory: [mem 0x00000000-0x00000fff]
	[    0.046902] PM: Registered nosave memory: [mem 0x0009d000-0x0009dfff]
	[    0.046902] PM: Registered nosave memory: [mem 0x0009e000-0x0009ffff]
	[    0.046902] PM: Registered nosave memory: [mem 0x000a0000-0x000dffff]
	[    0.046903] PM: Registered nosave memory: [mem 0x000e0000-0x000fffff]
	[    0.046903] PM: Registered nosave memory: [mem 0xcac87000-0xcac8dfff]
	[    0.046904] PM: Registered nosave memory: [mem 0xcb0d2000-0xcb662fff]
	[    0.046905] PM: Registered nosave memory: [mem 0xdd416000-0xdd4b1fff]
	[    0.046906] PM: Registered nosave memory: [mem 0xdd503000-0xdd63bfff]
	[    0.046906] PM: Registered nosave memory: [mem 0xdd63c000-0xdeffefff]
	[    0.046907] PM: Registered nosave memory: [mem 0xdf000000-0xf7ffffff]
	[    0.046908] PM: Registered nosave memory: [mem 0xf8000000-0xfbffffff]
	[    0.046908] PM: Registered nosave memory: [mem 0xfc000000-0xfebfffff]
	[    0.046908] PM: Registered nosave memory: [mem 0xfec00000-0xfec00fff]
	[    0.046909] PM: Registered nosave memory: [mem 0xfec01000-0xfecfffff]
	[    0.046909] PM: Registered nosave memory: [mem 0xfed00000-0xfed03fff]
	[    0.046909] PM: Registered nosave memory: [mem 0xfed04000-0xfed1bfff]
	[    0.046909] PM: Registered nosave memory: [mem 0xfed1c000-0xfed1ffff]
	[    0.046910] PM: Registered nosave memory: [mem 0xfed20000-0xfedfffff]
	[    0.046910] PM: Registered nosave memory: [mem 0xfee00000-0xfee00fff]
	[    0.046910] PM: Registered nosave memory: [mem 0xfee01000-0xfeffffff]
	[    0.046911] PM: Registered nosave memory: [mem 0xff000000-0xffffffff]
	[    0.046912] [mem 0xdf000000-0xf7ffffff] available for PCI devices
	[    0.046913] Booting paravirtualized kernel on bare hardware
	[    0.046915] clocksource: refined-jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645519600211568 ns
	[    0.046919] setup_percpu: NR_CPUS:8192 nr_cpumask_bits:8 nr_cpu_ids:8 nr_node_ids:1
	[    0.047076] percpu: Embedded 55 pages/cpu s188416 r8192 d28672 u262144
	[    0.047081] pcpu-alloc: s188416 r8192 d28672 u262144 alloc=1*2097152
	[    0.047081] pcpu-alloc: [0] 0 1 2 3 4 5 6 7
	[    0.047099] Built 1 zonelists, mobility grouping on.  Total pages: 4112219
	[    0.047100] Policy zone: Normal
	[    0.047100] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-5.4.0-88-generic root=UUID=1199f619-397d-4d1d-b2fb-512f97d76ee9 ro quiet splash vt.handoff=7
	[    0.047822] Dentry cache hash table entries: 2097152 (order: 12, 16777216 bytes, linear)
	[    0.048156] Inode-cache hash table entries: 1048576 (order: 11, 8388608 bytes, linear)
	[    0.048204] mem auto-init: stack:off, heap alloc:on, heap free:off
	[    0.050896] Calgary: detecting Calgary via BIOS EBDA area
	[    0.050897] Calgary: Unable to locate Rio Grande table in EBDA - bailing!
	[    0.085057] Memory: 16271696K/16710064K available (14339K kernel code, 2400K rwdata, 5016K rodata, 2728K init, 4972K bss, 438368K reserved, 0K cma-reserved)
	[    0.085062] random: get_random_u64 called from kmem_cache_open+0x2d/0x410 with crng_init=0
	[    0.085157] SLUB: HWalign=64, Order=0-3, MinObjects=0, CPUs=8, Nodes=1
	[    0.085166] Kernel/User page tables isolation: enabled
	[    0.085175] ftrace: allocating 44613 entries in 175 pages
	[    0.095878] rcu: Hierarchical RCU implementation.
	[    0.095879] rcu:     RCU restricting CPUs from NR_CPUS=8192 to nr_cpu_ids=8.
	[    0.095880]  Tasks RCU enabled.
	[    0.095880] rcu: RCU calculated value of scheduler-enlistment delay is 25 jiffies.
	[    0.095881] rcu: Adjusting geometry for rcu_fanout_leaf=16, nr_cpu_ids=8
	[    0.097690] NR_IRQS: 524544, nr_irqs: 488, preallocated irqs: 16
	[    0.097940] random: crng done (trusting CPU's manufacturer)
	[    0.097956] spurious 8259A interrupt: IRQ7.
	[    0.097963] vt handoff: transparent VT on vt#7
	[    0.097967] Console: colour dummy device 80x25
	[    0.097970] printk: console [tty0] enabled
	[    0.097982] ACPI: Core revision 20190816
	[    0.098058] clocksource: hpet: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 133484882848 ns
	[    0.098068] APIC: Switch to symmetric I/O mode setup
	[    0.098069] DMAR: Host address width 39
	[    0.098070] DMAR: DRHD base: 0x000000fed90000 flags: 0x1
	[    0.098073] DMAR: dmar0: reg_base_addr fed90000 ver 1:0 cap d2008c20660462 ecap f010da
	[    0.098074] DMAR: RMRR base: 0x000000dee97000 end: 0x000000deea5fff
	[    0.098075] DMAR-IR: IOAPIC id 8 under DRHD base  0xfed90000 IOMMU 0
	[    0.098076] DMAR-IR: HPET id 0 under DRHD base 0xfed90000
	[    0.098076] DMAR-IR: Queued invalidation will be enabled to support x2apic and Intr-remapping.
	[    0.098284] DMAR-IR: Enabled IRQ remapping in x2apic mode
	[    0.098285] x2apic enabled
	[    0.098290] Switched APIC routing to cluster x2apic.
	[    0.098676] ..TIMER: vector=0x30 apic1=0 pin1=2 apic2=-1 pin2=-1
	[    0.118069] clocksource: tsc-early: mask: 0xffffffffffffffff max_cycles: 0x735076aa906, max_idle_ns: 881591093595 ns
	[    0.118072] Calibrating delay loop (skipped), value calculated using timer frequency.. 7999.92 BogoMIPS (lpj=15999856)
	[    0.118073] pid_max: default: 32768 minimum: 301
	[    0.118094] LSM: Security Framework initializing
	[    0.118100] Yama: becoming mindful.
	[    0.118129] AppArmor: AppArmor initialized
	[    0.118172] Mount-cache hash table entries: 32768 (order: 6, 262144 bytes, linear)
	[    0.118197] Mountpoint-cache hash table entries: 32768 (order: 6, 262144 bytes, linear)
	[    0.118207] *** VALIDATE tmpfs ***
	[    0.118298] *** VALIDATE proc ***
	[    0.118331] *** VALIDATE cgroup1 ***
	[    0.118332] *** VALIDATE cgroup2 ***
	[    0.118370] mce: CPU0: Thermal monitoring enabled (TM1)
	[    0.118380] process: using mwait in idle threads
	[    0.118381] Last level iTLB entries: 4KB 1024, 2MB 1024, 4MB 1024
	[    0.118382] Last level dTLB entries: 4KB 1024, 2MB 1024, 4MB 1024, 1GB 4
	[    0.118383] Spectre V1 : Mitigation: usercopy/swapgs barriers and __user pointer sanitization
	[    0.118384] Spectre V2 : Mitigation: Full generic retpoline
	[    0.118384] Spectre V2 : Spectre v2 / SpectreRSB mitigation: Filling RSB on context switch
	[    0.118385] Spectre V2 : Enabling Restricted Speculation for firmware calls
	[    0.118385] Spectre V2 : mitigation: Enabling conditional Indirect Branch Prediction Barrier
	[    0.118386] Spectre V2 : User space: Mitigation: STIBP via seccomp and prctl
	[    0.118386] Speculative Store Bypass: Mitigation: Speculative Store Bypass disabled via prctl and seccomp
	[    0.118389] SRBDS: Mitigation: Microcode
	[    0.118389] MDS: Mitigation: Clear CPU buffers
	[    0.118506] Freeing SMP alternatives memory: 40K
	[    0.122120] smpboot: CPU0: Intel(R) Core(TM) i7-4790K CPU @ 4.00GHz (family: 0x6, model: 0x3c, stepping: 0x3)
	[    0.122193] Performance Events: PEBS fmt2+, Haswell events, 16-deep LBR, full-width counters, Intel PMU driver.
	[    0.122203] ... version:                3
	[    0.122204] ... bit width:              48
	[    0.122204] ... generic registers:      4
	[    0.122204] ... value mask:             0000ffffffffffff
	[    0.122205] ... max period:             00007fffffffffff
	[    0.122205] ... fixed-purpose events:   3
	[    0.122205] ... event mask:             000000070000000f
	[    0.122226] rcu: Hierarchical SRCU implementation.
	[    0.122901] NMI watchdog: Enabled. Permanently consumes one hw-PMU counter.
	[    0.122950] smp: Bringing up secondary CPUs ...
	[    0.123004] x86: Booting SMP configuration:
	[    0.123005] .... node  #0, CPUs:      #1 #2 #3 #4
	[    0.127413] MDS CPU bug present and SMT on, data leak possible. See https://www.kernel.org/doc/html/latest/admin-guide/hw-vuln/mds.html for more details.
	[    0.127413]  #5 #6 #7
	[    0.127413] smp: Brought up 1 node, 8 CPUs
	[    0.127413] smpboot: Max logical packages: 1
	[    0.127413] smpboot: Total of 8 processors activated (63999.42 BogoMIPS)
	[    0.130461] devtmpfs: initialized
	[    0.130461] x86/mm: Memory block size: 128MB
	[    0.131045] PM: Registering ACPI NVS region [mem 0xcac87000-0xcac8dfff] (28672 bytes)
	[    0.131045] PM: Registering ACPI NVS region [mem 0xdd503000-0xdd63bfff] (1282048 bytes)
	[    0.131045] clocksource: jiffies: mask: 0xffffffff max_cycles: 0xffffffff, max_idle_ns: 7645041785100000 ns
	[    0.131045] futex hash table entries: 2048 (order: 5, 131072 bytes, linear)
	[    0.131045] pinctrl core: initialized pinctrl subsystem
	[    0.131045] PM: RTC time: 20:03:00, date: 2021-10-11
	[    0.131045] NET: Registered protocol family 16
	[    0.131045] audit: initializing netlink subsys (disabled)
	[    0.131045] audit: type=2000 audit(1633982580.032:1): state=initialized audit_enabled=0 res=1
	[    0.131045] EISA bus registered
	[    0.131045] cpuidle: using governor ladder
	[    0.131045] cpuidle: using governor menu
	[    0.131045] ACPI FADT declares the system doesn't support PCIe ASPM, so disable it
	[    0.131045] ACPI: bus type PCI registered
	[    0.131045] acpiphp: ACPI Hot Plug PCI Controller Driver version: 0.5
	[    0.131045] PCI: MMCONFIG for domain 0000 [bus 00-3f] at [mem 0xf8000000-0xfbffffff] (base 0xf8000000)
	[    0.131045] PCI: MMCONFIG at [mem 0xf8000000-0xfbffffff] reserved in E820
	[    0.131045] PCI: Using configuration type 1 for base access
	[    0.131045] core: PMU erratum BJ122, BV98, HSD29 worked around, HT is on
	[    0.131511] HugeTLB registered 1.00 GiB page size, pre-allocated 0 pages
	[    0.131511] HugeTLB registered 2.00 MiB page size, pre-allocated 0 pages
	[    0.131511] ACPI: Added _OSI(Module Device)
	[    0.131511] ACPI: Added _OSI(Processor Device)
	[    0.131511] ACPI: Added _OSI(3.0 _SCP Extensions)
	[    0.131511] ACPI: Added _OSI(Processor Aggregator Device)
	[    0.131511] ACPI: Added _OSI(Linux-Dell-Video)
	[    0.131511] ACPI: Added _OSI(Linux-Lenovo-NV-HDMI-Audio)
	[    0.131511] ACPI: Added _OSI(Linux-HPI-Hybrid-Graphics)
	[    0.142176] ACPI: 6 ACPI AML tables successfully acquired and loaded
	[    0.143211] ACPI: [Firmware Bug]: BIOS _OSI(Linux) query ignored
	[    0.143935] ACPI: Dynamic OEM Table Load:
	[    0.143939] ACPI: SSDT 0xFFFF995A0C250800 0003D3 (v01 PmRef  Cpu0Cst  00003001 INTL 20120711)
	[    0.144662] ACPI: Dynamic OEM Table Load:
	[    0.144665] ACPI: SSDT 0xFFFF995A0BC44000 0005AA (v01 PmRef  ApIst    00003000 INTL 20120711)
	[    0.145419] ACPI: Dynamic OEM Table Load:
	[    0.145421] ACPI: SSDT 0xFFFF995A0C25EA00 000119 (v01 PmRef  ApCst    00003000 INTL 20120711)
	[    0.147308] ACPI: Interpreter enabled
	[    0.147326] ACPI: (supports S0 S3 S4 S5)
	[    0.147327] ACPI: Using IOAPIC for interrupt routing
	[    0.147346] PCI: Using host bridge windows from ACPI; if necessary, use "pci=nocrs" and report a bug
	[    0.147569] ACPI: Enabled 9 GPEs in block 00 to 3F
	[    0.154817] ACPI: Power Resource [FN00] (off)
	[    0.154886] ACPI: Power Resource [FN01] (off)
	[    0.154952] ACPI: Power Resource [FN02] (off)
	[    0.155019] ACPI: Power Resource [FN03] (off)
	[    0.155085] ACPI: Power Resource [FN04] (off)
	[    0.155696] ACPI: PCI Root Bridge [PCI0] (domain 0000 [bus 00-3e])
	[    0.155699] acpi PNP0A08:00: _OSC: OS supports [ExtendedConfig ASPM ClockPM Segments MSI HPX-Type3]
	[    0.155918] acpi PNP0A08:00: _OSC: platform does not support [PCIeHotplug SHPCHotplug PME]
	[    0.156047] acpi PNP0A08:00: _OSC: OS now controls [AER PCIeCapability LTR]
	[    0.156048] acpi PNP0A08:00: FADT indicates ASPM is unsupported, using BIOS configuration
	[    0.156389] PCI host bridge to bus 0000:00
	[    0.156390] pci_bus 0000:00: root bus resource [io  0x0000-0x0cf7 window]
	[    0.156391] pci_bus 0000:00: root bus resource [io  0x0d00-0xffff window]
	[    0.156391] pci_bus 0000:00: root bus resource [mem 0x000a0000-0x000bffff window]
	[    0.156392] pci_bus 0000:00: root bus resource [mem 0x000d0000-0x000d3fff window]
	[    0.156393] pci_bus 0000:00: root bus resource [mem 0x000d4000-0x000d7fff window]
	[    0.156393] pci_bus 0000:00: root bus resource [mem 0x000d8000-0x000dbfff window]
	[    0.156394] pci_bus 0000:00: root bus resource [mem 0x000dc000-0x000dffff window]
	[    0.156394] pci_bus 0000:00: root bus resource [mem 0x000e0000-0x000e3fff window]
	[    0.156395] pci_bus 0000:00: root bus resource [mem 0x000e4000-0x000e7fff window]
	[    0.156395] pci_bus 0000:00: root bus resource [mem 0xe0000000-0xfeafffff window]
	[    0.156396] pci_bus 0000:00: root bus resource [bus 00-3e]
	[    0.156402] pci 0000:00:00.0: [8086:0c00] type 00 class 0x060000
	[    0.156465] pci 0000:00:01.0: [8086:0c01] type 01 class 0x060400
	[    0.156493] pci 0000:00:01.0: PME# supported from D0 D3hot D3cold
	[    0.156605] pci 0000:00:14.0: [8086:8c31] type 00 class 0x0c0330
	[    0.156622] pci 0000:00:14.0: reg 0x10: [mem 0xf7300000-0xf730ffff 64bit]
	[    0.156671] pci 0000:00:14.0: PME# supported from D3hot D3cold
	[    0.156730] pci 0000:00:16.0: [8086:8c3a] type 00 class 0x078000
	[    0.156748] pci 0000:00:16.0: reg 0x10: [mem 0xf731a000-0xf731a00f 64bit]
	[    0.156798] pci 0000:00:16.0: PME# supported from D0 D3hot D3cold
	[    0.156856] pci 0000:00:1a.0: [8086:8c2d] type 00 class 0x0c0320
	[    0.156874] pci 0000:00:1a.0: reg 0x10: [mem 0xf7318000-0xf73183ff]
	[    0.156942] pci 0000:00:1a.0: PME# supported from D0 D3hot D3cold
	[    0.157004] pci 0000:00:1b.0: [8086:8c20] type 00 class 0x040300
	[    0.157020] pci 0000:00:1b.0: reg 0x10: [mem 0xf7310000-0xf7313fff 64bit]
	[    0.157078] pci 0000:00:1b.0: PME# supported from D0 D3hot D3cold
	[    0.157135] pci 0000:00:1c.0: [8086:8c10] type 01 class 0x060400
	[    0.157198] pci 0000:00:1c.0: PME# supported from D0 D3hot D3cold
	[    0.157297] pci 0000:00:1c.3: [8086:8c16] type 01 class 0x060400
	[    0.157362] pci 0000:00:1c.3: PME# supported from D0 D3hot D3cold
	[    0.157458] pci 0000:00:1c.7: [8086:8c1e] type 01 class 0x060400
	[    0.157523] pci 0000:00:1c.7: PME# supported from D0 D3hot D3cold
	[    0.157621] pci 0000:00:1d.0: [8086:8c26] type 00 class 0x0c0320
	[    0.157639] pci 0000:00:1d.0: reg 0x10: [mem 0xf7317000-0xf73173ff]
	[    0.157708] pci 0000:00:1d.0: PME# supported from D0 D3hot D3cold
	[    0.157772] pci 0000:00:1f.0: [8086:8c44] type 00 class 0x060100
	[    0.157914] pci 0000:00:1f.2: [8086:8c02] type 00 class 0x010601
	[    0.157926] pci 0000:00:1f.2: reg 0x10: [io  0xf070-0xf077]
	[    0.157932] pci 0000:00:1f.2: reg 0x14: [io  0xf060-0xf063]
	[    0.157937] pci 0000:00:1f.2: reg 0x18: [io  0xf050-0xf057]
	[    0.157943] pci 0000:00:1f.2: reg 0x1c: [io  0xf040-0xf043]
	[    0.157948] pci 0000:00:1f.2: reg 0x20: [io  0xf020-0xf03f]
	[    0.157954] pci 0000:00:1f.2: reg 0x24: [mem 0xf7316000-0xf73167ff]
	[    0.157981] pci 0000:00:1f.2: PME# supported from D3hot
	[    0.158035] pci 0000:00:1f.3: [8086:8c22] type 00 class 0x0c0500
	[    0.158049] pci 0000:00:1f.3: reg 0x10: [mem 0xf7315000-0xf73150ff 64bit]
	[    0.158065] pci 0000:00:1f.3: reg 0x20: [io  0xf000-0xf01f]
	[    0.158153] pci 0000:01:00.0: [10de:1dba] type 00 class 0x030000
	[    0.158164] pci 0000:01:00.0: reg 0x10: [mem 0xf6000000-0xf6ffffff]
	[    0.158170] pci 0000:01:00.0: reg 0x14: [mem 0xe0000000-0xefffffff 64bit pref]
	[    0.158176] pci 0000:01:00.0: reg 0x1c: [mem 0xf0000000-0xf1ffffff 64bit pref]
	[    0.158180] pci 0000:01:00.0: reg 0x24: [io  0xe000-0xe07f]
	[    0.158183] pci 0000:01:00.0: reg 0x30: [mem 0xf7000000-0xf707ffff pref]
	[    0.158257] pci 0000:01:00.1: [10de:10f2] type 00 class 0x040300
	[    0.158265] pci 0000:01:00.1: reg 0x10: [mem 0xf7080000-0xf7083fff]
	[    0.158345] pci 0000:00:01.0: PCI bridge to [bus 01]
	[    0.158346] pci 0000:00:01.0:   bridge window [io  0xe000-0xefff]
	[    0.158347] pci 0000:00:01.0:   bridge window [mem 0xf6000000-0xf70fffff]
	[    0.158349] pci 0000:00:01.0:   bridge window [mem 0xe0000000-0xf1ffffff 64bit pref]
	[    0.158392] acpiphp: Slot [1] registered
	[    0.158396] pci 0000:00:1c.0: PCI bridge to [bus 02]
	[    0.158452] pci 0000:03:00.0: [1969:e091] type 00 class 0x020000
	[    0.158483] pci 0000:03:00.0: reg 0x10: [mem 0xf7200000-0xf723ffff 64bit]
	[    0.158495] pci 0000:03:00.0: reg 0x18: [io  0xd000-0xd07f]
	[    0.158603] pci 0000:03:00.0: PME# supported from D0 D1 D2 D3hot D3cold
	[    0.158691] pci 0000:00:1c.3: PCI bridge to [bus 03]
	[    0.158693] pci 0000:00:1c.3:   bridge window [io  0xd000-0xdfff]
	[    0.158696] pci 0000:00:1c.3:   bridge window [mem 0xf7200000-0xf72fffff]
	[    0.158751] pci 0000:04:00.0: [1b21:0612] type 00 class 0x010601
	[    0.158773] pci 0000:04:00.0: reg 0x10: [io  0xc050-0xc057]
	[    0.158782] pci 0000:04:00.0: reg 0x14: [io  0xc040-0xc043]
	[    0.158792] pci 0000:04:00.0: reg 0x18: [io  0xc030-0xc037]
	[    0.158802] pci 0000:04:00.0: reg 0x1c: [io  0xc020-0xc023]
	[    0.158811] pci 0000:04:00.0: reg 0x20: [io  0xc000-0xc01f]
	[    0.158821] pci 0000:04:00.0: reg 0x24: [mem 0xf7100000-0xf71001ff]
	[    0.158954] pci 0000:00:1c.7: PCI bridge to [bus 04]
	[    0.158957] pci 0000:00:1c.7:   bridge window [io  0xc000-0xcfff]
	[    0.158959] pci 0000:00:1c.7:   bridge window [mem 0xf7100000-0xf71fffff]
	[    0.159563] ACPI: PCI Interrupt Link [LNKA] (IRQs 3 4 5 6 10 *11 12 14 15)
	[    0.159608] ACPI: PCI Interrupt Link [LNKB] (IRQs 3 4 5 6 *10 11 12 14 15)
	[    0.159651] ACPI: PCI Interrupt Link [LNKC] (IRQs 3 4 5 6 *10 11 12 14 15)
	[    0.159693] ACPI: PCI Interrupt Link [LNKD] (IRQs 3 4 *5 6 10 11 12 14 15)
	[    0.159735] ACPI: PCI Interrupt Link [LNKE] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
	[    0.159777] ACPI: PCI Interrupt Link [LNKF] (IRQs 3 4 5 6 10 11 12 14 15) *0, disabled.
	[    0.159820] ACPI: PCI Interrupt Link [LNKG] (IRQs *3 4 5 6 10 11 12 14 15)
	[    0.159864] ACPI: PCI Interrupt Link [LNKH] (IRQs 3 4 5 6 10 *11 12 14 15)
	[    0.160177] iommu: Default domain type: Translated
	[    0.160177] SCSI subsystem initialized
	[    0.160177] libata version 3.00 loaded.
	[    0.160177] pci 0000:01:00.0: vgaarb: setting as boot VGA device
	[    0.160177] pci 0000:01:00.0: vgaarb: VGA device added: decodes=io+mem,owns=io+mem,locks=none
	[    0.160177] pci 0000:01:00.0: vgaarb: bridge control possible
	[    0.160177] vgaarb: loaded
	[    0.160177] ACPI: bus type USB registered
	[    0.160177] usbcore: registered new interface driver usbfs
	[    0.160177] usbcore: registered new interface driver hub
	[    0.160177] usbcore: registered new device driver usb
	[    0.160177] pps_core: LinuxPPS API ver. 1 registered
	[    0.160177] pps_core: Software ver. 5.3.6 - Copyright 2005-2007 Rodolfo Giometti <giometti@linux.it>
	[    0.160177] PTP clock support registered
	[    0.160177] EDAC MC: Ver: 3.0.0
	[    0.160177] PCI: Using ACPI for IRQ routing
	[    0.160177] PCI: pci_cache_line_size set to 64 bytes
	[    0.160177] e820: reserve RAM buffer [mem 0x0009d800-0x0009ffff]
	[    0.160177] e820: reserve RAM buffer [mem 0xcac87000-0xcbffffff]
	[    0.160177] e820: reserve RAM buffer [mem 0xcb0d2000-0xcbffffff]
	[    0.160177] e820: reserve RAM buffer [mem 0xdd416000-0xdfffffff]
	[    0.160177] e820: reserve RAM buffer [mem 0xdd503000-0xdfffffff]
	[    0.160177] e820: reserve RAM buffer [mem 0xdf000000-0xdfffffff]
	[    0.160177] e820: reserve RAM buffer [mem 0x41f000000-0x41fffffff]
	[    0.160177] NetLabel: Initializing
	[    0.160177] NetLabel:  domain hash size = 128
	[    0.160177] NetLabel:  protocols = UNLABELED CIPSOv4 CALIPSO
	[    0.160177] NetLabel:  unlabeled traffic allowed by default
	[    0.162280] hpet0: at MMIO 0xfed00000, IRQs 2, 8, 0, 0, 0, 0, 0, 0
	[    0.162283] hpet0: 8 comparators, 64-bit 14.318180 MHz counter
	[    0.164302] clocksource: Switched to clocksource tsc-early
	[    0.167844] *** VALIDATE bpf ***
	[    0.167844] VFS: Disk quotas dquot_6.6.0
	[    0.167844] VFS: Dquot-cache hash table entries: 512 (order 0, 4096 bytes)
	[    0.167844] *** VALIDATE ramfs ***
	[    0.167844] *** VALIDATE hugetlbfs ***
	[    0.167844] AppArmor: AppArmor Filesystem Enabled
	[    0.167844] pnp: PnP ACPI init
	[    0.167844] system 00:00: [mem 0xfed40000-0xfed44fff] has been reserved
	[    0.167844] system 00:00: Plug and Play ACPI device, IDs PNP0c01 (active)
	[    0.167844] system 00:01: [io  0x0680-0x069f] has been reserved
	[    0.167844] system 00:01: [io  0xffff] has been reserved
	[    0.167844] system 00:01: [io  0xffff] has been reserved
	[    0.167844] system 00:01: [io  0xffff] has been reserved
	[    0.167844] system 00:01: [io  0x1c00-0x1cfe] has been reserved
	[    0.167844] system 00:01: [io  0x1d00-0x1dfe] has been reserved
	[    0.167844] system 00:01: [io  0x1e00-0x1efe] has been reserved
	[    0.167844] system 00:01: [io  0x1f00-0x1ffe] has been reserved
	[    0.167844] system 00:01: [io  0x1800-0x18fe] has been reserved
	[    0.167844] system 00:01: [io  0x164e-0x164f] has been reserved
	[    0.167844] system 00:01: Plug and Play ACPI device, IDs PNP0c02 (active)
	[    0.167844] pnp 00:02: Plug and Play ACPI device, IDs PNP0b00 (active)
	[    0.167844] system 00:03: [io  0x1854-0x1857] has been reserved
	[    0.167844] system 00:03: Plug and Play ACPI device, IDs INT3f0d PNP0c02 (active)
	[    0.170144] system 00:04: [io  0x0a00-0x0a0f] has been reserved
	[    0.170145] system 00:04: [io  0x0a10-0x0a1f] has been reserved
	[    0.170147] system 00:04: Plug and Play ACPI device, IDs PNP0c02 (active)
	[    0.170283] pnp 00:05: [dma 0 disabled]
	[    0.170308] pnp 00:05: Plug and Play ACPI device, IDs PNP0501 (active)
	[    0.170343] system 00:06: [io  0x04d0-0x04d1] has been reserved
	[    0.170345] system 00:06: Plug and Play ACPI device, IDs PNP0c02 (active)
	[    0.170704] system 00:07: [mem 0xfed1c000-0xfed1ffff] has been reserved
	[    0.170704] system 00:07: [mem 0xfed10000-0xfed17fff] has been reserved
	[    0.170705] system 00:07: [mem 0xfed18000-0xfed18fff] has been reserved
	[    0.170706] system 00:07: [mem 0xfed19000-0xfed19fff] has been reserved
	[    0.170706] system 00:07: [mem 0xf8000000-0xfbffffff] has been reserved
	[    0.170707] system 00:07: [mem 0xfed20000-0xfed3ffff] has been reserved
	[    0.170708] system 00:07: [mem 0xfed90000-0xfed93fff] could not be reserved
	[    0.170709] system 00:07: [mem 0xfed45000-0xfed8ffff] has been reserved
	[    0.170709] system 00:07: [mem 0xff000000-0xffffffff] has been reserved
	[    0.170710] system 00:07: [mem 0xfee00000-0xfeefffff] could not be reserved
	[    0.170711] system 00:07: [mem 0xf7fdf000-0xf7fdffff] has been reserved
	[    0.170712] system 00:07: [mem 0xf7fe0000-0xf7feffff] has been reserved
	[    0.170713] system 00:07: Plug and Play ACPI device, IDs PNP0c02 (active)
	[    0.170911] pnp: PnP ACPI: found 8 devices
	[    0.171610] thermal_sys: Registered thermal governor 'fair_share'
	[    0.171611] thermal_sys: Registered thermal governor 'bang_bang'
	[    0.171611] thermal_sys: Registered thermal governor 'step_wise'
	[    0.171611] thermal_sys: Registered thermal governor 'user_space'
	[    0.171612] thermal_sys: Registered thermal governor 'power_allocator'
	[    0.176099] clocksource: acpi_pm: mask: 0xffffff max_cycles: 0xffffff, max_idle_ns: 2085701024 ns
	[    0.176121] pci 0000:00:01.0: PCI bridge to [bus 01]
	[    0.176123] pci 0000:00:01.0:   bridge window [io  0xe000-0xefff]
	[    0.176124] pci 0000:00:01.0:   bridge window [mem 0xf6000000-0xf70fffff]
	[    0.176126] pci 0000:00:01.0:   bridge window [mem 0xe0000000-0xf1ffffff 64bit pref]
	[    0.176128] pci 0000:00:1c.0: PCI bridge to [bus 02]
	[    0.176136] pci 0000:00:1c.3: PCI bridge to [bus 03]
	[    0.176138] pci 0000:00:1c.3:   bridge window [io  0xd000-0xdfff]
	[    0.176141] pci 0000:00:1c.3:   bridge window [mem 0xf7200000-0xf72fffff]
	[    0.176147] pci 0000:00:1c.7: PCI bridge to [bus 04]
	[    0.176148] pci 0000:00:1c.7:   bridge window [io  0xc000-0xcfff]
	[    0.176151] pci 0000:00:1c.7:   bridge window [mem 0xf7100000-0xf71fffff]
	[    0.176157] pci_bus 0000:00: resource 4 [io  0x0000-0x0cf7 window]
	[    0.176158] pci_bus 0000:00: resource 5 [io  0x0d00-0xffff window]
	[    0.176159] pci_bus 0000:00: resource 6 [mem 0x000a0000-0x000bffff window]
	[    0.176159] pci_bus 0000:00: resource 7 [mem 0x000d0000-0x000d3fff window]
	[    0.176160] pci_bus 0000:00: resource 8 [mem 0x000d4000-0x000d7fff window]
	[    0.176161] pci_bus 0000:00: resource 9 [mem 0x000d8000-0x000dbfff window]
	[    0.176161] pci_bus 0000:00: resource 10 [mem 0x000dc000-0x000dffff window]
	[    0.176162] pci_bus 0000:00: resource 11 [mem 0x000e0000-0x000e3fff window]
	[    0.176162] pci_bus 0000:00: resource 12 [mem 0x000e4000-0x000e7fff window]
	[    0.176163] pci_bus 0000:00: resource 13 [mem 0xe0000000-0xfeafffff window]
	[    0.176164] pci_bus 0000:01: resource 0 [io  0xe000-0xefff]
	[    0.176164] pci_bus 0000:01: resource 1 [mem 0xf6000000-0xf70fffff]
	[    0.176165] pci_bus 0000:01: resource 2 [mem 0xe0000000-0xf1ffffff 64bit pref]
	[    0.176166] pci_bus 0000:03: resource 0 [io  0xd000-0xdfff]
	[    0.176166] pci_bus 0000:03: resource 1 [mem 0xf7200000-0xf72fffff]
	[    0.176167] pci_bus 0000:04: resource 0 [io  0xc000-0xcfff]
	[    0.176167] pci_bus 0000:04: resource 1 [mem 0xf7100000-0xf71fffff]
	[    0.176245] NET: Registered protocol family 2
	[    0.176349] IP idents hash table entries: 262144 (order: 9, 2097152 bytes, linear)
	[    0.177626] tcp_listen_portaddr_hash hash table entries: 8192 (order: 5, 131072 bytes, linear)
	[    0.177683] TCP established hash table entries: 131072 (order: 8, 1048576 bytes, linear)
	[    0.177820] TCP bind hash table entries: 65536 (order: 8, 1048576 bytes, linear)
	[    0.177908] TCP: Hash tables configured (established 131072 bind 65536)
	[    0.177939] UDP hash table entries: 8192 (order: 6, 262144 bytes, linear)
	[    0.177967] UDP-Lite hash table entries: 8192 (order: 6, 262144 bytes, linear)
	[    0.178010] NET: Registered protocol family 1
	[    0.178013] NET: Registered protocol family 44
	[    0.178373] pci 0000:01:00.0: Video device with shadowed ROM at [mem 0x000c0000-0x000dffff]
	[    0.178379] pci 0000:01:00.1: D0 power state depends on 0000:01:00.0
	[    0.178383] pci 0000:03:00.0: set MSI_INTX_DISABLE_BUG flag
	[    0.178388] PCI: CLS 64 bytes, default 64
	[    0.178439] Trying to unpack rootfs image as initramfs...
	[    0.253955] Freeing initrd memory: 50836K
	[    0.274079] PCI-DMA: Using software bounce buffering for IO (SWIOTLB)
	[    0.274081] software IO TLB: mapped [mem 0xd9416000-0xdd416000] (64MB)
	[    0.274278] check: Scanning for low memory corruption every 60 seconds
	[    0.274574] Initialise system trusted keyrings
	[    0.274584] Key type blacklist registered
	[    0.274603] workingset: timestamp_bits=36 max_order=22 bucket_order=0
	[    0.275351] zbud: loaded
	[    0.275564] squashfs: version 4.0 (2009/01/31) Phillip Lougher
	[    0.275651] fuse: init (API version 7.31)
	[    0.275660] *** VALIDATE fuse ***
	[    0.275661] *** VALIDATE fuse ***
	[    0.275716] Platform Keyring initialized
	[    0.278307] Key type asymmetric registered
	[    0.278307] Asymmetric key parser 'x509' registered
	[    0.278312] Block layer SCSI generic (bsg) driver version 0.4 loaded (major 244)
	[    0.278329] io scheduler mq-deadline registered
	[    0.278848] shpchp: Standard Hot Plug PCI Controller Driver version: 0.4
	[    0.278881] vesafb: mode is 640x480x32, linelength=2560, pages=0
	[    0.278882] vesafb: scrolling: redraw
	[    0.278883] vesafb: Truecolor: size=8:8:8:8, shift=24:16:8:0
	[    0.278890] vesafb: framebuffer at 0xf1000000, mapped to 0x00000000d0b7a9fe, using 1216k, total 1216k
	[    0.278912] fbcon: Deferring console take-over
	[    0.278912] fb0: VESA VGA frame buffer device
	[    0.278919] intel_idle: MWAIT substates: 0x42120
	[    0.278920] intel_idle: v0.4.1 model 0x3C
	[    0.279125] intel_idle: lapic_timer_reliable_states 0xffffffff
	[    0.279217] input: Power Button as /devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0C:00/input/input0
	[    0.279240] ACPI: Power Button [PWRB]
	[    0.279261] input: Power Button as /devices/LNXSYSTM:00/LNXPWRBN:00/input/input1
	[    0.279274] ACPI: Power Button [PWRF]
	[    0.279885] thermal LNXTHERM:00: registered as thermal_zone0
	[    0.279886] ACPI: Thermal Zone [TZ00] (28 C)
	[    0.280078] thermal LNXTHERM:01: registered as thermal_zone1
	[    0.280079] ACPI: Thermal Zone [TZ01] (30 C)
	[    0.280157] Serial: 8250/16550 driver, 32 ports, IRQ sharing enabled
	[    0.300557] 00:05: ttyS0 at I/O 0x3f8 (irq = 4, base_baud = 115200) is a 16550A
	[    0.301514] Linux agpgart interface v0.103
	[    0.454118] loop: module loaded
	[    0.454309] libphy: Fixed MDIO Bus: probed
	[    0.454309] tun: Universal TUN/TAP device driver, 1.6
	[    0.454387] PPP generic driver version 2.4.2
	[    0.454584] VFIO - User Level meta-driver version: 0.3
	[    0.454702] ehci_hcd: USB 2.0 'Enhanced' Host Controller (EHCI) Driver
	[    0.454705] ehci-pci: EHCI PCI platform driver
	[    0.454778] ehci-pci 0000:00:1a.0: EHCI Host Controller
	[    0.454782] ehci-pci 0000:00:1a.0: new USB bus registered, assigned bus number 1
	[    0.454791] ehci-pci 0000:00:1a.0: debug port 2
	[    0.458691] ehci-pci 0000:00:1a.0: cache line size of 64 is not supported
	[    0.458700] ehci-pci 0000:00:1a.0: irq 16, io mem 0xf7318000
	[    0.474111] ehci-pci 0000:00:1a.0: USB 2.0 started, EHCI 1.00
	[    0.474142] usb usb1: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
	[    0.474143] usb usb1: New USB device strings: Mfr=3, Product=2, SerialNumber=1
	[    0.474143] usb usb1: Product: EHCI Host Controller
	[    0.474144] usb usb1: Manufacturer: Linux 5.4.0-88-generic ehci_hcd
	[    0.474145] usb usb1: SerialNumber: 0000:00:1a.0
	[    0.474278] hub 1-0:1.0: USB hub found
	[    0.474281] hub 1-0:1.0: 2 ports detected
	[    0.474435] ehci-pci 0000:00:1d.0: EHCI Host Controller
	[    0.474437] ehci-pci 0000:00:1d.0: new USB bus registered, assigned bus number 2
	[    0.474445] ehci-pci 0000:00:1d.0: debug port 2
	[    0.478343] ehci-pci 0000:00:1d.0: cache line size of 64 is not supported
	[    0.478351] ehci-pci 0000:00:1d.0: irq 23, io mem 0xf7317000
	[    0.494110] ehci-pci 0000:00:1d.0: USB 2.0 started, EHCI 1.00
	[    0.494130] usb usb2: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
	[    0.494131] usb usb2: New USB device strings: Mfr=3, Product=2, SerialNumber=1
	[    0.494131] usb usb2: Product: EHCI Host Controller
	[    0.494132] usb usb2: Manufacturer: Linux 5.4.0-88-generic ehci_hcd
	[    0.494132] usb usb2: SerialNumber: 0000:00:1d.0
	[    0.494260] hub 2-0:1.0: USB hub found
	[    0.494263] hub 2-0:1.0: 2 ports detected
	[    0.494351] ehci-platform: EHCI generic platform driver
	[    0.494356] ohci_hcd: USB 1.1 'Open' Host Controller (OHCI) Driver
	[    0.494358] ohci-pci: OHCI PCI platform driver
	[    0.494363] ohci-platform: OHCI generic platform driver
	[    0.494367] uhci_hcd: USB Universal Host Controller Interface driver
	[    0.494434] xhci_hcd 0000:00:14.0: xHCI Host Controller
	[    0.494436] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 3
	[    0.495479] xhci_hcd 0000:00:14.0: hcc params 0x200077c1 hci version 0x100 quirks 0x0000000000009810
	[    0.495482] xhci_hcd 0000:00:14.0: cache line size of 64 is not supported
	[    0.495581] usb usb3: New USB device found, idVendor=1d6b, idProduct=0002, bcdDevice= 5.04
	[    0.495581] usb usb3: New USB device strings: Mfr=3, Product=2, SerialNumber=1
	[    0.495582] usb usb3: Product: xHCI Host Controller
	[    0.495583] usb usb3: Manufacturer: Linux 5.4.0-88-generic xhci-hcd
	[    0.495583] usb usb3: SerialNumber: 0000:00:14.0
	[    0.495711] hub 3-0:1.0: USB hub found
	[    0.495725] hub 3-0:1.0: 14 ports detected
	[    0.497723] xhci_hcd 0000:00:14.0: xHCI Host Controller
	[    0.497725] xhci_hcd 0000:00:14.0: new USB bus registered, assigned bus number 4
	[    0.497726] xhci_hcd 0000:00:14.0: Host supports USB 3.0 SuperSpeed
	[    0.497748] usb usb4: New USB device found, idVendor=1d6b, idProduct=0003, bcdDevice= 5.04
	[    0.497749] usb usb4: New USB device strings: Mfr=3, Product=2, SerialNumber=1
	[    0.497750] usb usb4: Product: xHCI Host Controller
	[    0.497750] usb usb4: Manufacturer: Linux 5.4.0-88-generic xhci-hcd
	[    0.497751] usb usb4: SerialNumber: 0000:00:14.0
	[    0.497815] hub 4-0:1.0: USB hub found
	[    0.497825] hub 4-0:1.0: 6 ports detected
	[    0.498242] i8042: PNP: No PS/2 controller found.
	[    0.498422] mousedev: PS/2 mouse device common for all mice
	[    0.498597] rtc_cmos 00:02: RTC can wake from S4
	[    0.498745] rtc_cmos 00:02: registered as rtc0
	[    0.498753] rtc_cmos 00:02: alarms up to one month, y3k, 242 bytes nvram, hpet irqs
	[    0.498757] i2c /dev entries driver
	[    0.498776] device-mapper: uevent: version 1.0.3
	[    0.498820] device-mapper: ioctl: 4.41.0-ioctl (2019-09-16) initialised: dm-devel@redhat.com
	[    0.498832] platform eisa.0: Probing EISA bus 0
	[    0.498832] platform eisa.0: EISA: Cannot allocate resource for mainboard
	[    0.498833] platform eisa.0: Cannot allocate resource for EISA slot 1
	[    0.498834] platform eisa.0: Cannot allocate resource for EISA slot 2
	[    0.498834] platform eisa.0: Cannot allocate resource for EISA slot 3
	[    0.498835] platform eisa.0: Cannot allocate resource for EISA slot 4
	[    0.498835] platform eisa.0: Cannot allocate resource for EISA slot 5
	[    0.498836] platform eisa.0: Cannot allocate resource for EISA slot 6
	[    0.498836] platform eisa.0: Cannot allocate resource for EISA slot 7
	[    0.498837] platform eisa.0: Cannot allocate resource for EISA slot 8
	[    0.498837] platform eisa.0: EISA: Detected 0 cards
	[    0.498841] intel_pstate: Intel P-state driver initializing
	[    0.499401] ledtrig-cpu: registered to indicate activity on CPUs
	[    0.499450] drop_monitor: Initializing network drop monitor service
	[    0.499543] NET: Registered protocol family 10
	[    0.503524] Segment Routing with IPv6
	[    0.503546] NET: Registered protocol family 17
	[    0.503654] Key type dns_resolver registered
	[    0.504077] RAS: Correctable Errors collector initialized.
	[    0.504105] microcode: sig=0x306c3, pf=0x2, revision=0x28
	[    0.504259] microcode: Microcode Update Driver: v2.2.
	[    0.504261] IPI shorthand broadcast: enabled
	[    0.504265] sched_clock: Marking stable (504049209, 208022)->(526648838, -22391607)
	[    0.504374] registered taskstats version 1
	[    0.504379] Loading compiled-in X.509 certificates
	[    0.504856] Loaded X.509 cert 'Build time autogenerated kernel key: 92f0bd9ca5683f6b296baf0cd33861a222c877ca'
	[    0.505250] Loaded X.509 cert 'Canonical Ltd. Live Patch Signing: 14df34d1a87cf37625abec039ef2bf521249b969'
	[    0.505641] Loaded X.509 cert 'Canonical Ltd. Kernel Module Signing: 88f752e560a1e0737e31163a466ad7b70a850c19'
	[    0.505663] zswap: loaded using pool lzo/zbud
	[    0.505722] Key type ._fscrypt registered
	[    0.505722] Key type .fscrypt registered
	[    0.509082] Key type big_key registered
	[    0.510850] Key type encrypted registered
	[    0.510852] AppArmor: AppArmor sha1 policy hashing enabled
	[    0.510855] ima: No TPM chip found, activating TPM-bypass!
	[    0.510885] ima: Allocated hash algorithm: sha1
	[    0.510889] ima: No architecture policies found
	[    0.510893] evm: Initialising EVM extended attributes:
	[    0.510894] evm: security.selinux
	[    0.510894] evm: security.SMACK64
	[    0.510894] evm: security.SMACK64EXEC
	[    0.510894] evm: security.SMACK64TRANSMUTE
	[    0.510895] evm: security.SMACK64MMAP
	[    0.510895] evm: security.apparmor
	[    0.510895] evm: security.ima
	[    0.510896] evm: security.capability
	[    0.510896] evm: HMAC attrs: 0x1
	[    0.511266] PM:   Magic number: 9:486:93
	[    0.511375] rtc_cmos 00:02: setting system clock to 2021-10-11T20:03:00 UTC (1633982580)
	[    0.512064] Freeing unused decrypted memory: 2040K
	[    0.512346] Freeing unused kernel image memory: 2728K
	[    0.594127] Write protecting the kernel read-only data: 22528k
	[    0.594479] Freeing unused kernel image memory: 2008K
	[    0.594593] Freeing unused kernel image memory: 1128K
	[    0.600550] x86/mm: Checked W+X mappings: passed, no W+X pages found.
	[    0.600551] x86/mm: Checking user space page tables
	[    0.606074] x86/mm: Checked W+X mappings: passed, no W+X pages found.
	[    0.606075] Run /init as init process
	[    0.663444] ACPI Warning: SystemIO range 0x0000000000001828-0x000000000000182F conflicts with OpRegion 0x0000000000001800-0x000000000000187F (\PMIO) (20190816/utaddress-204)
	[    0.663450] ACPI: If an ACPI driver is available for this device, you should use it instead of the native driver
	[    0.663453] ACPI Warning: SystemIO range 0x0000000000001C40-0x0000000000001C4F conflicts with OpRegion 0x0000000000001C00-0x0000000000001FFF (\GPR) (20190816/utaddress-204)
	[    0.663456] ACPI: If an ACPI driver is available for this device, you should use it instead of the native driver
	[    0.663457] ACPI Warning: SystemIO range 0x0000000000001C30-0x0000000000001C3F conflicts with OpRegion 0x0000000000001C00-0x0000000000001C3F (\GPRL) (20190816/utaddress-204)
	[    0.663460] ACPI Warning: SystemIO range 0x0000000000001C30-0x0000000000001C3F conflicts with OpRegion 0x0000000000001C00-0x0000000000001FFF (\GPR) (20190816/utaddress-204)
	[    0.663463] ACPI: If an ACPI driver is available for this device, you should use it instead of the native driver
	[    0.663464] ACPI Warning: SystemIO range 0x0000000000001C00-0x0000000000001C2F conflicts with OpRegion 0x0000000000001C00-0x0000000000001C3F (\GPRL) (20190816/utaddress-204)
	[    0.663467] ACPI Warning: SystemIO range 0x0000000000001C00-0x0000000000001C2F conflicts with OpRegion 0x0000000000001C00-0x0000000000001FFF (\GPR) (20190816/utaddress-204)
	[    0.663470] ACPI: If an ACPI driver is available for this device, you should use it instead of the native driver
	[    0.663470] lpc_ich: Resource conflict(s) found affecting gpio_ich
	[    0.664500] i801_smbus 0000:00:1f.3: SPD Write Disable is set
	[    0.664527] i801_smbus 0000:00:1f.3: SMBus using PCI interrupt
	[    0.665290] ahci 0000:00:1f.2: version 3.0
	[    0.665458] ahci 0000:00:1f.2: AHCI 0001.0300 32 slots 6 ports 6 Gbps 0x20 impl SATA mode
	[    0.665461] ahci 0000:00:1f.2: flags: 64bit ncq led clo pio slum part ems apst
	[    0.673990] scsi host0: ahci
	[    0.674354] scsi host1: ahci
	[    0.674418] scsi host2: ahci
	[    0.674778] scsi host3: ahci
	[    0.674857] scsi host4: ahci
	[    0.676676] alx 0000:03:00.0 eth0: Qualcomm Atheros AR816x/AR817x Ethernet [44:8a:5b:89:6d:3b]
	[    0.678572] scsi host5: ahci
	[    0.678618] ata1: DUMMY
	[    0.678619] ata2: DUMMY
	[    0.678619] ata3: DUMMY
	[    0.678619] ata4: DUMMY
	[    0.678620] ata5: DUMMY
	[    0.678621] ata6: SATA max UDMA/133 abar m2048@0xf7316000 port 0xf7316380 irq 30
	[    0.678762] ahci 0000:04:00.0: SSS flag set, parallel bus scan disabled
	[    0.678816] ahci 0000:04:00.0: AHCI 0001.0200 32 slots 2 ports 6 Gbps 0x3 impl SATA mode
	[    0.678817] ahci 0000:04:00.0: flags: 64bit ncq sntf stag led clo pmp pio slum part ccc sxs
	[    0.678881] alx 0000:03:00.0 enp3s0: renamed from eth0
	[    0.678960] scsi host6: ahci
	[    0.679012] scsi host7: ahci
	[    0.679042] ata7: SATA max UDMA/133 abar m512@0xf7100000 port 0xf7100100 irq 31
	[    0.679044] ata8: SATA max UDMA/133 abar m512@0xf7100000 port 0xf7100180 irq 31
	[    0.814108] usb 1-1: new high-speed USB device number 2 using ehci-pci
	[    0.830109] usb 3-3: new high-speed USB device number 2 using xhci_hcd
	[    0.830114] usb 2-1: new high-speed USB device number 2 using ehci-pci
	[    0.970530] usb 1-1: New USB device found, idVendor=8087, idProduct=8008, bcdDevice= 0.05
	[    0.970531] usb 1-1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
	[    0.970836] hub 1-1:1.0: USB hub found
	[    0.971029] hub 1-1:1.0: 6 ports detected
	[    0.982306] usb 3-3: New USB device found, idVendor=0451, idProduct=8042, bcdDevice= 1.00
	[    0.982306] usb 3-3: New USB device strings: Mfr=0, Product=0, SerialNumber=0
	[    0.982907] hub 3-3:1.0: USB hub found
	[    0.982929] hub 3-3:1.0: 4 ports detected
	[    0.994139] ata6: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
	[    0.994530] usb 2-1: New USB device found, idVendor=8087, idProduct=8000, bcdDevice= 0.05
	[    0.994531] usb 2-1: New USB device strings: Mfr=0, Product=0, SerialNumber=0
	[    0.994814] hub 2-1:1.0: USB hub found
	[    0.994914] hub 2-1:1.0: 8 ports detected
	[    0.995105] ACPI BIOS Error (bug): Could not resolve symbol [\_SB.PCI0.SAT0.SPT5._GTF.DSSP], AE_NOT_FOUND (20190816/psargs-330)
	[    0.995110] No Local Variables are initialized for Method [_GTF]
	[    0.995111] No Arguments are initialized for method [_GTF]
	[    0.995112] ACPI Error: Aborting method \_SB.PCI0.SAT0.SPT5._GTF due to previous error (AE_NOT_FOUND) (20190816/psparse-529)
	[    0.995362] ata6.00: ATA-8: TOSHIBA HDWD130, MX6OACF0, max UDMA/133
	[    0.995363] ata6.00: 5860533168 sectors, multi 16: LBA48 NCQ (depth 32), AA
	[    0.996414] ACPI BIOS Error (bug): Could not resolve symbol [\_SB.PCI0.SAT0.SPT5._GTF.DSSP], AE_NOT_FOUND (20190816/psargs-330)
	[    0.996420] No Local Variables are initialized for Method [_GTF]
	[    0.996420] No Arguments are initialized for method [_GTF]
	[    0.996421] ACPI Error: Aborting method \_SB.PCI0.SAT0.SPT5._GTF due to previous error (AE_NOT_FOUND) (20190816/psparse-529)
	[    0.996663] ata6.00: configured for UDMA/133
	[    0.996771] scsi 5:0:0:0: Direct-Access     ATA      TOSHIBA HDWD130  ACF0 PQ: 0 ANSI: 5
	[    0.996975] sd 5:0:0:0: Attached scsi generic sg0 type 0
	[    0.996993] sd 5:0:0:0: [sda] 5860533168 512-byte logical blocks: (3.00 TB/2.73 TiB)
	[    0.996995] sd 5:0:0:0: [sda] 4096-byte physical blocks
	[    0.996998] sd 5:0:0:0: [sda] Write Protect is off
	[    0.996999] sd 5:0:0:0: [sda] Mode Sense: 00 3a 00 00
	[    0.997004] sd 5:0:0:0: [sda] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
	[    1.055499]  sda: sda1
	[    1.074171] sd 5:0:0:0: [sda] Attached SCSI disk
	[    1.162114] ata7: SATA link up 6.0 Gbps (SStatus 133 SControl 300)
	[    1.162298] ata7.00: ATA-9: TOSHIBA-TR150, SAFZ12.3, max UDMA/133
	[    1.162298] ata7.00: 468862128 sectors, multi 16: LBA48 NCQ (depth 32), AA
	[    1.162573] ata7.00: configured for UDMA/133
	[    1.162638] scsi 6:0:0:0: Direct-Access     ATA      TOSHIBA-TR150    12.3 PQ: 0 ANSI: 5
	[    1.162751] sd 6:0:0:0: Attached scsi generic sg1 type 0
	[    1.162810] sd 6:0:0:0: [sdb] 468862128 512-byte logical blocks: (240 GB/224 GiB)
	[    1.162820] sd 6:0:0:0: [sdb] Write Protect is off
	[    1.162821] sd 6:0:0:0: [sdb] Mode Sense: 00 3a 00 00
	[    1.162838] sd 6:0:0:0: [sdb] Write cache: enabled, read cache: enabled, doesn't support DPO or FUA
	[    1.182666]  sdb: sdb1
	[    1.198622] sd 6:0:0:0: [sdb] Attached SCSI disk
	[    1.270107] usb 3-3.1: new low-speed USB device number 3 using xhci_hcd
	[    1.282106] tsc: Refined TSC clocksource calibration: 3999.996 MHz
	[    1.282110] clocksource: tsc: mask: 0xffffffffffffffff max_cycles: 0x7350b459580, max_idle_ns: 881591204237 ns
	[    1.282134] clocksource: Switched to clocksource tsc
	[    1.373778] usb 3-3.1: New USB device found, idVendor=0461, idProduct=4e22, bcdDevice= 1.00
	[    1.373779] usb 3-3.1: New USB device strings: Mfr=1, Product=2, SerialNumber=0
	[    1.373791] usb 3-3.1: Product: USB Optical Mouse
	[    1.373792] usb 3-3.1: Manufacturer: PixArt
	[    1.378762] hidraw: raw HID events driver (C) Jiri Kosina
	[    1.381016] usbcore: registered new interface driver usbhid
	[    1.381017] usbhid: USB HID core driver
	[    1.382550] input: PixArt USB Optical Mouse as /devices/pci0000:00/0000:00:14.0/usb3/3-3/3-3.1/3-3.1:1.0/0003:0461:4E22.0001/input/input2
	[    1.382668] hid-generic 0003:0461:4E22.0001: input,hidraw0: USB HID v1.11 Mouse [PixArt USB Optical Mouse] on usb-0000:00:14.0-3.1/input0
	[    1.454105] usb 3-3.2: new low-speed USB device number 4 using xhci_hcd
	[    1.476767] ata8: SATA link down (SStatus 0 SControl 300)
	[    1.559284] usb 3-3.2: New USB device found, idVendor=413c, idProduct=2107, bcdDevice= 1.78
	[    1.559285] usb 3-3.2: New USB device strings: Mfr=1, Product=2, SerialNumber=0
	[    1.559295] usb 3-3.2: Product: Dell USB Entry Keyboard
	[    1.559296] usb 3-3.2: Manufacturer: DELL
	[    1.564789] input: DELL Dell USB Entry Keyboard as /devices/pci0000:00/0000:00:14.0/usb3/3-3/3-3.2/3-3.2:1.0/0003:413C:2107.0002/input/input3
	[    1.622148] hid-generic 0003:413C:2107.0002: input,hidraw1: USB HID v1.10 Keyboard [DELL Dell USB Entry Keyboard] on usb-0000:00:14.0-3.2/input0
	[    1.688914] fbcon: Taking over console
	[    1.688948] Console: switching to colour frame buffer device 80x30
	[    1.695643] EXT4-fs (sdb1): mounted filesystem with ordered data mode. Opts: (null)
	[    1.844256] systemd[1]: Inserted module 'autofs4'
	[    1.857450] systemd[1]: systemd 245.4-4ubuntu3.13 running in system mode. (+PAM +AUDIT +SELINUX +IMA +APPARMOR +SMACK +SYSVINIT +UTMP +LIBCRYPTSETUP +GCRYPT +GNUTLS +ACL +XZ +LZ4 +SECCOMP +BLKID +ELFUTILS +KMOD +IDN2 -IDN +PCRE2 default-hierarchy=hybrid)
	[    1.874168] systemd[1]: Detected architecture x86-64.
	[    1.898977] systemd[1]: Set hostname to <vislab-inwin>.
	[    2.031215] systemd[1]: Created slice system-modprobe.slice.
	[    2.031336] systemd[1]: Created slice User and Session Slice.
	[    2.031371] systemd[1]: Started Forward Password Requests to Wall Directory Watch.
	[    2.031490] systemd[1]: Set up automount Arbitrary Executable File Formats File System Automount Point.
	[    2.031510] systemd[1]: Reached target User and Group Name Lookups.
	[    2.031516] systemd[1]: Reached target Remote File Systems.
	[    2.031524] systemd[1]: Reached target Slices.
	[    2.031587] systemd[1]: Listening on Syslog Socket.
	[    2.031629] systemd[1]: Listening on fsck to fsckd communication Socket.
	[    2.031662] systemd[1]: Listening on initctl Compatibility Named Pipe.
	[    2.031757] systemd[1]: Listening on Journal Audit Socket.
	[    2.031798] systemd[1]: Listening on Journal Socket (/dev/log).
	[    2.031852] systemd[1]: Listening on Journal Socket.
	[    2.031904] systemd[1]: Listening on udev Control Socket.
	[    2.031936] systemd[1]: Listening on udev Kernel Socket.
	[    2.032398] systemd[1]: Mounting Huge Pages File System...
	[    2.032951] systemd[1]: Mounting POSIX Message Queue File System...
	[    2.033553] systemd[1]: Mounting Kernel Debug File System...
	[    2.034095] systemd[1]: Mounting Kernel Trace File System...
	[    2.034853] systemd[1]: Starting Journal Service...
	[    2.035381] systemd[1]: Starting Set the console keyboard layout...
	[    2.036022] systemd[1]: Starting Create list of static device nodes for the current kernel...
	[    2.036871] systemd[1]: Starting Load Kernel Module drm...
	[    2.037702] systemd[1]: Condition check resulted in Set Up Additional Binary Formats being skipped.
	[    2.037729] systemd[1]: Condition check resulted in File System Check on Root Device being skipped.
	[    2.039105] systemd[1]: Starting Load Kernel Modules...
	[    2.039762] systemd[1]: Starting Remount Root and Kernel File Systems...
	[    2.040318] systemd[1]: Starting udev Coldplug all Devices...
	[    2.040951] systemd[1]: Starting Uncomplicated firewall...
	[    2.041747] systemd[1]: Started Read required files in advance.
	[    2.043423] systemd[1]: Mounted Huge Pages File System.
	[    2.043540] systemd[1]: Mounted POSIX Message Queue File System.
	[    2.043643] systemd[1]: Mounted Kernel Debug File System.
	[    2.043756] systemd[1]: Mounted Kernel Trace File System.
	[    2.044108] systemd[1]: Finished Create list of static device nodes for the current kernel.
	[    2.046783] systemd[1]: Finished Uncomplicated firewall.
	[    2.049516] EXT4-fs (sdb1): re-mounted. Opts: errors=remount-ro
	[    2.050491] systemd[1]: Finished Remount Root and Kernel File Systems.
	[    2.050721] systemd[1]: modprobe@drm.service: Succeeded.
	[    2.050989] systemd[1]: Finished Load Kernel Module drm.
	[    2.051793] systemd[1]: Activating swap /swapfile...
	[    2.053094] systemd[1]: Condition check resulted in Rebuild Hardware Database being skipped.
	[    2.053143] systemd[1]: Condition check resulted in Platform Persistent Storage Archival being skipped.
	[    2.053868] systemd[1]: Starting Load/Save Random Seed...
	[    2.054673] systemd[1]: Starting Create System Users...
	[    2.059021] lp: driver loaded but no devices found
	[    2.065130] ppdev: user-space parallel port driver
	[    2.073631] systemd[1]: Finished Load/Save Random Seed.
	[    2.079182] systemd[1]: Finished Load Kernel Modules.
	[    2.080068] systemd[1]: Mounting FUSE Control File System...
	[    2.080893] systemd[1]: Mounting Kernel Configuration File System...
	[    2.082163] systemd[1]: Starting Apply Kernel Variables...
	[    2.083568] systemd[1]: Mounted FUSE Control File System.
	[    2.083692] systemd[1]: Mounted Kernel Configuration File System.
	[    2.087863] systemd[1]: Finished Create System Users.
	[    2.088602] systemd[1]: Starting Create Static Device Nodes in /dev...
	[    2.091591] systemd[1]: Started Journal Service.
	[    2.097377] systemd-journald[312]: Received client request to flush runtime journal.
	[    2.130092] Adding 2097148k swap on /swapfile.  Priority:-2 extents:6 across:2260988k SSFS
	[    2.627234] RAPL PMU: API unit is 2^-32 Joules, 3 fixed counters, 655360 ms ovfl timer
	[    2.627236] RAPL PMU: hw unit of domain pp0-core 2^-14 Joules
	[    2.627236] RAPL PMU: hw unit of domain package 2^-14 Joules
	[    2.627237] RAPL PMU: hw unit of domain dram 2^-14 Joules
	[    2.683442] cryptd: max_cpu_qlen set to 1000
	[    2.748576] AVX2 version of gcm_enc/dec engaged.
	[    2.748577] AES CTR mode by8 optimization enabled
	[    2.827024] MXM: GUID detected in BIOS
	[    2.827199] checking generic (f1000000 130000) vs hw (e0000000 10000000)
	[    2.827200] checking generic (f1000000 130000) vs hw (f0000000 2000000)
	[    2.827201] fb0: switching to nouveaufb from VESA VGA
	[    2.828309] Console: switching to colour dummy device 80x25
	[    2.828404] nouveau 0000:01:00.0: NVIDIA GV100 (140000a1)
	[    2.947500] nouveau 0000:01:00.0: bios: version 88.00.3b.00.0a
	[    2.965038] intel_rapl_common: Found RAPL domain package
	[    2.965039] intel_rapl_common: Found RAPL domain core
	[    2.965040] intel_rapl_common: Found RAPL domain dram
	[    3.109335] snd_hda_intel 0000:01:00.1: Disabling MSI
	[    3.109339] snd_hda_intel 0000:01:00.1: Handle vga_switcheroo audio client
	[    3.405460] snd_hda_codec_realtek hdaudioC0D0: ALC1150: SKU not ready 0x00000000
	[    3.405956] snd_hda_codec_realtek hdaudioC0D0: autoconfig for ALC1150: line_outs=4 (0x14/0x15/0x16/0x17/0x0) type:line
	[    3.405957] snd_hda_codec_realtek hdaudioC0D0:    speaker_outs=0 (0x0/0x0/0x0/0x0/0x0)
	[    3.405958] snd_hda_codec_realtek hdaudioC0D0:    hp_outs=1 (0x1b/0x0/0x0/0x0/0x0)
	[    3.405958] snd_hda_codec_realtek hdaudioC0D0:    mono: mono_out=0x0
	[    3.405959] snd_hda_codec_realtek hdaudioC0D0:    dig-out=0x1e/0x0
	[    3.405959] snd_hda_codec_realtek hdaudioC0D0:    inputs:
	[    3.405960] snd_hda_codec_realtek hdaudioC0D0:      Front Mic=0x19
	[    3.405961] snd_hda_codec_realtek hdaudioC0D0:      Rear Mic=0x18
	[    3.405961] snd_hda_codec_realtek hdaudioC0D0:      Line=0x1a
	[    3.419558] input: HDA Intel PCH Front Mic as /devices/pci0000:00/0000:00:1b.0/sound/card0/input4
	[    3.419613] input: HDA Intel PCH Rear Mic as /devices/pci0000:00/0000:00:1b.0/sound/card0/input5
	[    3.419658] input: HDA Intel PCH Line as /devices/pci0000:00/0000:00:1b.0/sound/card0/input6
	[    3.419714] input: HDA Intel PCH Line Out Front as /devices/pci0000:00/0000:00:1b.0/sound/card0/input7
	[    3.419756] input: HDA Intel PCH Line Out Surround as /devices/pci0000:00/0000:00:1b.0/sound/card0/input8
	[    3.419792] input: HDA Intel PCH Line Out CLFE as /devices/pci0000:00/0000:00:1b.0/sound/card0/input9
	[    3.419864] input: HDA Intel PCH Line Out Side as /devices/pci0000:00/0000:00:1b.0/sound/card0/input10
	[    3.419925] input: HDA Intel PCH Front Headphone as /devices/pci0000:00/0000:00:1b.0/sound/card0/input11
	[    3.426808] nouveau 0000:01:00.0: bios: M0203T type 04
	[    3.426810] nouveau 0000:01:00.0: bios: M0203E not matched!
	[    3.426866] nouveau 0000:01:00.0: fb: 32768 MiB of unknown memory type
	[    3.464931] [TTM] Zone  kernel: Available graphics memory: 8165238 KiB
	[    3.464932] [TTM] Zone   dma32: Available graphics memory: 2097152 KiB
	[    3.464933] [TTM] Initializing pool allocator
	[    3.464935] [TTM] Initializing DMA pool allocator
	[    3.464945] nouveau 0000:01:00.0: DRM: VRAM: 32768 MiB
	[    3.464946] nouveau 0000:01:00.0: DRM: GART: 536870912 MiB
	[    3.464948] nouveau 0000:01:00.0: DRM: BIT table 'A' not found
	[    3.464948] nouveau 0000:01:00.0: DRM: BIT table 'L' not found
	[    3.464949] nouveau 0000:01:00.0: DRM: TMDS table version 2.0
	[    3.464950] nouveau 0000:01:00.0: DRM: DCB version 4.1
	[    3.464951] nouveau 0000:01:00.0: DRM: DCB outp 00: 02800f56 04600010
	[    3.464952] nouveau 0000:01:00.0: DRM: DCB outp 01: 02000f52 00020010
	[    3.464952] nouveau 0000:01:00.0: DRM: DCB outp 02: 02811f66 04600020
	[    3.464953] nouveau 0000:01:00.0: DRM: DCB outp 03: 02011f62 00020020
	[    3.464953] nouveau 0000:01:00.0: DRM: DCB outp 04: 04822f76 04600010
	[    3.464954] nouveau 0000:01:00.0: DRM: DCB outp 05: 04022f72 00020010
	[    3.464955] nouveau 0000:01:00.0: DRM: DCB outp 06: 04833f86 04600020
	[    3.464955] nouveau 0000:01:00.0: DRM: DCB outp 07: 04033f82 00020020
	[    3.464956] nouveau 0000:01:00.0: DRM: DCB conn 00: 00010046
	[    3.464956] nouveau 0000:01:00.0: DRM: DCB conn 01: 00020146
	[    3.464957] nouveau 0000:01:00.0: DRM: DCB conn 02: 01000246
	[    3.464957] nouveau 0000:01:00.0: DRM: DCB conn 03: 02000346
	[    3.464958] nouveau 0000:01:00.0: DRM: DCB conn 04: 00000460
	[    3.465331] nouveau 0000:01:00.0: DRM: MM: using COPY for buffer copies
	[    3.587824] [drm] Supports vblank timestamp caching Rev 2 (21.10.2013).
	[    3.587826] [drm] Driver supports precise vblank timestamp query.
	[    4.124771] audit: type=1400 audit(1633982584.106:2): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/sbin/cups-browsed" pid=717 comm="apparmor_parser"
	[    4.124774] audit: type=1400 audit(1633982584.106:3): apparmor="STATUS" operation="profile_load" profile="unconfined" name="libreoffice-oopslash" pid=712 comm="apparmor_parser"
	[    4.126789] audit: type=1400 audit(1633982584.110:4): apparmor="STATUS" operation="profile_load" profile="unconfined" name="ippusbxd" pid=716 comm="apparmor_parser"
	[    4.126953] audit: type=1400 audit(1633982584.110:5): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/snapd/snap-confine" pid=714 comm="apparmor_parser"
	[    4.126956] audit: type=1400 audit(1633982584.110:6): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/snapd/snap-confine//mount-namespace-capture-helper" pid=714 comm="apparmor_parser"
	[    4.127268] audit: type=1400 audit(1633982584.110:7): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-client.action" pid=715 comm="apparmor_parser"
	[    4.127270] audit: type=1400 audit(1633982584.110:8): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/NetworkManager/nm-dhcp-helper" pid=715 comm="apparmor_parser"
	[    4.127272] audit: type=1400 audit(1633982584.110:9): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/usr/lib/connman/scripts/dhclient-script" pid=715 comm="apparmor_parser"
	[    4.127274] audit: type=1400 audit(1633982584.110:10): apparmor="STATUS" operation="profile_load" profile="unconfined" name="/{,usr/}sbin/dhclient" pid=715 comm="apparmor_parser"
	[    4.432194] nouveau 0000:01:00.0: DRM: allocated 1920x1080 fb: 0x200000, bo 0000000078d283ed
	[    4.432644] fbcon: nouveaudrmfb (fb0) is primary device
	[    4.432721] Console: switching to colour frame buffer device 240x67
	[    4.432746] nouveau 0000:01:00.0: fb0: nouveaudrmfb frame buffer device
	[    4.630107] alx 0000:03:00.0 enp3s0: NIC Up: 1 Gbps Full
	[    4.630360] IPv6: ADDRCONF(NETDEV_CHANGE): enp3s0: link becomes ready
	[    4.751011] [drm] Initialized nouveau 1.3.1 20120801 for 0000:01:00.0 on minor 0
	[    4.918218] input: HDA NVidia HDMI/DP,pcm=3 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input12
	[    4.918277] input: HDA NVidia HDMI/DP,pcm=7 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input13
	[    4.918312] input: HDA NVidia HDMI/DP,pcm=8 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input14
	[    4.918374] input: HDA NVidia HDMI/DP,pcm=9 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input15
	[    4.918475] input: HDA NVidia HDMI/DP,pcm=10 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input16
	[    4.918554] input: HDA NVidia HDMI/DP,pcm=11 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input17
	[    4.918630] input: HDA NVidia HDMI/DP,pcm=12 as /devices/pci0000:00/0000:00:01.0/0000:01:00.1/sound/card1/input18
	[   10.016452] rfkill: input handler disabled
	[   22.697207] rfkill: input handler enabled
```

```shell
(base) ╭─vislab at vislab-inwin in ~/Code 21-10-11 - 17:01:41
	╰─○ more /var/log/Xorg.0.log
	[     6.052] (--) Log file renamed from "/var/log/Xorg.pid-985.log" to "/var/log/Xorg.0.log"
	[     6.053]
	X.Org X Server 1.20.11
	X Protocol Version 11, Revision 0
	[     6.053] Build Operating System: linux Ubuntu
	[     6.053] Current Operating System: Linux vislab-inwin 5.4.0-88-generic #99-Ubuntu SMP Thu Sep 23 17:29:00 UTC 2021 x86_64
	[     6.053] Kernel command line: BOOT_IMAGE=/boot/vmlinuz-5.4.0-88-generic root=UUID=1199f619-397d-4d1d-b2fb-512f97d76ee9 ro quiet spl
	ash vt.handoff=7
	[     6.053] Build Date: 06 July 2021  10:17:51AM
	[     6.053] xorg-server 2:1.20.11-1ubuntu1~20.04.2 (For technical support please see http://www.ubuntu.com/support)
	[     6.053] Current version of pixman: 0.38.4
	[     6.053]    Before reporting problems, check http://wiki.x.org
					to make sure that you have the latest version.
	[     6.053] Markers: (--) probed, (**) from config file, (==) default setting,
					(++) from command line, (!!) notice, (II) informational,
					(WW) warning, (EE) error, (NI) not implemented, (??) unknown.
	[     6.053] (==) Log file: "/var/log/Xorg.0.log", Time: Mon Oct 11 14:50:16 2021
	[     6.053] (==) Using system config directory "/usr/share/X11/xorg.conf.d"
	[     6.054] (==) No Layout section.  Using the first Screen section.
	[     6.054] (==) No screen section available. Using defaults.
	[     6.054] (**) |-->Screen "Default Screen Section" (0)
	[     6.054] (**) |   |-->Monitor "<default monitor>"
	[     6.054] (==) No monitor specified for screen "Default Screen Section".
					Using a default monitor configuration.
	[     6.054] (==) Automatically adding devices
	[     6.054] (==) Automatically enabling devices
	[     6.054] (==) Automatically adding GPU devices
	[     6.054] (==) Automatically binding GPU devices
	[     6.054] (==) Max clients allowed: 256, resource mask: 0x1fffff
	[     6.054] (WW) The directory "/usr/share/fonts/X11/cyrillic" does not exist.
	[     6.054]    Entry deleted from font path.
	[     6.054] (WW) The directory "/usr/share/fonts/X11/100dpi/" does not exist.
	[     6.054]    Entry deleted from font path.
	[     6.054] (WW) The directory "/usr/share/fonts/X11/75dpi/" does not exist.
	[     6.054]    Entry deleted from font path.
	[     6.054] (WW) The directory "/usr/share/fonts/X11/100dpi" does not exist.
	[     6.054]    Entry deleted from font path.
	[     6.054] (WW) The directory "/usr/share/fonts/X11/75dpi" does not exist.
	[     6.054]    Entry deleted from font path.
	[     6.054] (==) FontPath set to:
					/usr/share/fonts/X11/misc,
					/usr/share/fonts/X11/Type1,
					built-ins
	[     6.054] (==) ModulePath set to "/usr/lib/xorg/modules"
	[     6.054] (II) The server relies on udev to provide the list of input devices.
					If no devices become available, reconfigure udev or disable AutoAddDevices.
	[     6.054] (II) Loader magic: 0x55e4ed719020
	[     6.054] (II) Module ABI versions:
	[     6.054]    X.Org ANSI C Emulation: 0.4
	[     6.054]    X.Org Video Driver: 24.1
	[     6.054]    X.Org XInput driver : 24.1
	[     6.054]    X.Org Server Extension : 10.0
	[     6.055] (++) using VT number 1

	[     6.056] (II) systemd-logind: took control of session /org/freedesktop/login1/session/c1
	[     6.056] (II) xfree86: Adding drm device (/dev/dri/card0)
	[     6.057] (II) systemd-logind: got fd for /dev/dri/card0 226:0 fd 12 paused 0
	[     6.057] (**) OutputClass "nvidia" ModulePath extended to "/usr/lib/x86_64-linux-gnu/nvidia/xorg,/usr/lib/xorg/modules"
	[     6.058] (--) PCI:*(1@0:0:0) 10de:1dba:10de:121a rev 161, Mem @ 0xf6000000/16777216, 0xe0000000/268435456, 0xf0000000/33554432, I/O
	 @ 0x0000e000/128, BIOS @ 0x????????/131072
	[     6.058] (II) LoadModule: "glx"
	[     6.058] (II) Loading /usr/lib/xorg/modules/extensions/libglx.so
	[     6.059] (II) Module glx: vendor="X.Org Foundation"
	[     6.059]    compiled for 1.20.11, module version = 1.0.0
	[     6.059]    ABI class: X.Org Server Extension, version 10.0
	[     6.059] (II) Applying OutputClass "nvidia" to /dev/dri/card0
	[     6.059]    loading driver: nvidia
	[     6.287] (==) Matched nvidia as autoconfigured driver 0
	[     6.287] (==) Matched nouveau as autoconfigured driver 1
	[     6.287] (==) Matched modesetting as autoconfigured driver 2
	[     6.287] (==) Matched fbdev as autoconfigured driver 3
	[     6.287] (==) Matched vesa as autoconfigured driver 4
	[     6.287] (==) Assigned the driver to the xf86ConfigLayout
	[     6.287] (II) LoadModule: "nvidia"
	[     6.287] (II) Loading /usr/lib/x86_64-linux-gnu/nvidia/xorg/nvidia_drv.so
	[     6.288] (II) Module nvidia: vendor="NVIDIA Corporation"
	[     6.288]    compiled for 1.6.99.901, module version = 1.0.0
	[     6.288]    Module class: X.Org Video Driver
	[     6.288] (II) LoadModule: "nouveau"
	[     6.288] (II) Loading /usr/lib/xorg/modules/drivers/nouveau_drv.so
	[     6.288] (II) Module nouveau: vendor="X.Org Foundation"
	[     6.288]    compiled for 1.20.3, module version = 1.0.16
	[     6.288]    Module class: X.Org Video Driver
	[     6.288]    ABI class: X.Org Video Driver, version 24.0
	[     6.288] (II) LoadModule: "modesetting"
	[     6.288] (II) Loading /usr/lib/xorg/modules/drivers/modesetting_drv.so
	[     6.288] (II) Module modesetting: vendor="X.Org Foundation"
	[     6.288]    compiled for 1.20.11, module version = 1.20.11
	[     6.288]    Module class: X.Org Video Driver
	[     6.288]    ABI class: X.Org Video Driver, version 24.1
	[     6.288] (II) LoadModule: "fbdev"
	[     6.288] (II) Loading /usr/lib/xorg/modules/drivers/fbdev_drv.so
	[     6.288] (II) Module fbdev: vendor="X.Org Foundation"
	[     6.288]    compiled for 1.20.1, module version = 0.5.0
	[     6.288]    Module class: X.Org Video Driver
	[     6.288]    ABI class: X.Org Video Driver, version 24.0
	[     6.288] (II) LoadModule: "vesa"
	[     6.288] (II) Loading /usr/lib/xorg/modules/drivers/vesa_drv.so
	[     6.288] (II) Module vesa: vendor="X.Org Foundation"
	[     6.288]    compiled for 1.20.4, module version = 2.4.0
	[     6.288]    Module class: X.Org Video Driver
	[     6.288]    ABI class: X.Org Video Driver, version 24.0
	[     6.288] (II) NVIDIA dlloader X Driver  460.91.03  Fri Jul  2 05:48:55 UTC 2021
	[     6.288] (II) NVIDIA Unified Driver for all Supported NVIDIA GPUs
	[     6.288] (II) NOUVEAU driver Date:   Mon Jan 28 23:25:58 2019 -0500
	[     6.288] (II) NOUVEAU driver for NVIDIA chipset families :
	[     6.288]    RIVA TNT            (NV04)
	[     6.288]    RIVA TNT2           (NV05)
	[     6.288]    GeForce 256         (NV10)
	[     6.288]    GeForce 2           (NV11, NV15)
	[     6.288]    GeForce 4MX         (NV17, NV18)
	[     6.289]    GeForce 3           (NV20)
	[     6.289]    GeForce 4Ti         (NV25, NV28)
	[     6.289]    GeForce FX          (NV3x)
	[     6.289]    GeForce 6           (NV4x)
	[     6.289]    GeForce 7           (G7x)
	[     6.289]    GeForce 8           (G8x)
	[     6.289]    GeForce 9           (G9x)
	[     6.289]    GeForce GTX 2xx/3xx (GT2xx)
	[     6.289]    GeForce GTX 4xx/5xx (GFxxx)
	[     6.289]    GeForce GTX 6xx/7xx (GKxxx)
	[     6.289]    GeForce GTX 9xx     (GMxxx)
	[     6.289]    GeForce GTX 10xx    (GPxxx)
	[     6.289] (II) modesetting: Driver for Modesetting Kernel Drivers: kms
	[     6.289] (II) FBDEV: driver for framebuffer: fbdev
	[     6.289] (II) VESA: driver for VESA chipsets: vesa
	[     6.289] (II) systemd-logind: releasing fd for 226:0
	[     6.289] (II) Loading sub module "fb"
	[     6.289] (II) LoadModule: "fb"
	[     6.289] (II) Loading /usr/lib/xorg/modules/libfb.so
	[     6.289] (II) Module fb: vendor="X.Org Foundation"
	[     6.289]    compiled for 1.20.11, module version = 1.0.0
	[     6.289]    ABI class: X.Org ANSI C Emulation, version 0.4
	[     6.289] (II) Loading sub module "wfb"
	[     6.289] (II) LoadModule: "wfb"
	[     6.290] (II) Loading /usr/lib/xorg/modules/libwfb.so
	[     6.290] (II) Module wfb: vendor="X.Org Foundation"
	[     6.290]    compiled for 1.20.11, module version = 1.0.0
	[     6.290]    ABI class: X.Org ANSI C Emulation, version 0.4
	[     6.290] (II) Loading sub module "ramdac"
	[     6.290] (II) LoadModule: "ramdac"
	[     6.290] (II) Module "ramdac" already built-in
	[     6.290] (WW) Falling back to old probe method for modesetting
	[     6.290] (WW) Falling back to old probe method for fbdev
	[     6.290] (II) Loading sub module "fbdevhw"
	[     6.290] (II) LoadModule: "fbdevhw"
	[     6.290] (II) Loading /usr/lib/xorg/modules/libfbdevhw.so
	[     6.290] (II) Module fbdevhw: vendor="X.Org Foundation"
	[     6.290]    compiled for 1.20.11, module version = 0.0.2
	[     6.290]    ABI class: X.Org Video Driver, version 24.1
	[     6.290] (II) NVIDIA(0): Creating default Display subsection in Screen section
					"Default Screen Section" for depth/fbbpp 24/32
	[     6.290] (==) NVIDIA(0): Depth 24, (==) framebuffer bpp 32
	[     6.290] (==) NVIDIA(0): RGB weight 888
	[     6.290] (==) NVIDIA(0): Default visual is TrueColor
	[     6.290] (==) NVIDIA(0): Using gamma correction (1.0, 1.0, 1.0)
	[     6.290] (II) Applying OutputClass "nvidia" options to /dev/dri/card0
	[     6.290] (**) NVIDIA(0): Option "AllowEmptyInitialConfiguration"
	[     6.290] (**) NVIDIA(0): Enabling 2D acceleration
	[     6.290] (II) Loading sub module "glxserver_nvidia"
	[     6.291] (II) LoadModule: "glxserver_nvidia"
	[     6.291] (II) Loading /usr/lib/x86_64-linux-gnu/nvidia/xorg/libglxserver_nvidia.so
	[     6.328] (II) Module glxserver_nvidia: vendor="NVIDIA Corporation"
	[     6.328]    compiled for 1.6.99.901, module version = 1.0.0
	[     6.328]    Module class: X.Org Server Extension
	[     6.328] (II) NVIDIA GLX Module  460.91.03  Fri Jul  2 05:46:33 UTC 2021
	[     6.328] (II) NVIDIA: The X server supports PRIME Render Offload.
	[     7.306] (--) NVIDIA(0): Valid display device(s) on GPU-0 at PCI:1:0:0
	[     7.306] (--) NVIDIA(0):     DFP-0
	[     7.306] (--) NVIDIA(0):     DFP-1 (boot)
	[     7.306] (--) NVIDIA(0):     DFP-2
	[     7.306] (--) NVIDIA(0):     DFP-3
	[     7.306] (--) NVIDIA(0):     DFP-4
	[     7.306] (--) NVIDIA(0):     DFP-5
	[     7.306] (--) NVIDIA(0):     DFP-6
	[     7.306] (--) NVIDIA(0):     DFP-7
	[     7.307] (II) NVIDIA(0): NVIDIA GPU Quadro GV100 (GV100GL-A) at PCI:1:0:0 (GPU-0)
	[     7.307] (--) NVIDIA(0): Memory: 33554432 kBytes
	[     7.307] (--) NVIDIA(0): VideoBIOS: 88.00.3b.00.0a
	[     7.307] (II) NVIDIA(0): Detected PCI Express Link width: 16X
	[     7.307] (--) NVIDIA(GPU-0): DFP-0: disconnected
	[     7.307] (--) NVIDIA(GPU-0): DFP-0: Internal DisplayPort
	[     7.307] (--) NVIDIA(GPU-0): DFP-0: 1440.0 MHz maximum pixel clock
	[     7.307] (--) NVIDIA(GPU-0):
	[     7.369] (--) NVIDIA(GPU-0): Samsung SMS27A850 (DFP-1): connected
	[     7.369] (--) NVIDIA(GPU-0): Samsung SMS27A850 (DFP-1): Internal TMDS
	[     7.369] (--) NVIDIA(GPU-0): Samsung SMS27A850 (DFP-1): 165.0 MHz maximum pixel clock
	[     7.369] (--) NVIDIA(GPU-0):
	[     7.369] (--) NVIDIA(GPU-0): DFP-2: disconnected
	[     7.369] (--) NVIDIA(GPU-0): DFP-2: Internal DisplayPort
	[     7.369] (--) NVIDIA(GPU-0): DFP-2: 1440.0 MHz maximum pixel clock
	[     7.369] (--) NVIDIA(GPU-0):
	[     7.369] (--) NVIDIA(GPU-0): DFP-3: disconnected
	[     7.369] (--) NVIDIA(GPU-0): DFP-3: Internal TMDS
	[     7.369] (--) NVIDIA(GPU-0): DFP-3: 165.0 MHz maximum pixel clock
	[     7.369] (--) NVIDIA(GPU-0):
	[     7.369] (--) NVIDIA(GPU-0): DFP-4: disconnected
	[     7.369] (--) NVIDIA(GPU-0): DFP-4: Internal DisplayPort
	[     7.369] (--) NVIDIA(GPU-0): DFP-4: 1440.0 MHz maximum pixel clock
	[     7.369] (--) NVIDIA(GPU-0):
	[     7.369] (--) NVIDIA(GPU-0): DFP-5: disconnected
	[     7.369] (--) NVIDIA(GPU-0): DFP-5: Internal TMDS
	[     7.369] (--) NVIDIA(GPU-0): DFP-5: 165.0 MHz maximum pixel clock
	[     7.369] (--) NVIDIA(GPU-0):
	[     7.369] (--) NVIDIA(GPU-0): DFP-6: disconnected
	[     7.369] (--) NVIDIA(GPU-0): DFP-6: Internal DisplayPort
	[     7.369] (--) NVIDIA(GPU-0): DFP-6: 1440.0 MHz maximum pixel clock
	[     7.370] (--) NVIDIA(GPU-0):
	[     7.370] (--) NVIDIA(GPU-0): DFP-7: disconnected
	[     7.370] (--) NVIDIA(GPU-0): DFP-7: Internal TMDS
	[     7.370] (--) NVIDIA(GPU-0): DFP-7: 165.0 MHz maximum pixel clock
	[     7.370] (--) NVIDIA(GPU-0):
	[     7.373] (==) NVIDIA(0):
	[     7.373] (==) NVIDIA(0): No modes were requested; the default mode "nvidia-auto-select"
	[     7.373] (==) NVIDIA(0):     will be used as the requested mode.
	[     7.373] (==) NVIDIA(0):
	[     7.374] (II) NVIDIA(0): Validated MetaModes:
	[     7.374] (II) NVIDIA(0):     "DFP-1:nvidia-auto-select"
	[     7.374] (II) NVIDIA(0): Virtual screen size determined to be 1920 x 1080
	[     7.376] (--) NVIDIA(0): DPI set to (93, 85); computed from "UseEdidDpi" X config
	[     7.376] (--) NVIDIA(0):     option
	[     7.376] (II) UnloadModule: "nouveau"
	[     7.376] (II) Unloading nouveau
	[     7.376] (II) UnloadModule: "modesetting"
	[     7.376] (II) Unloading modesetting
	[     7.376] (II) UnloadModule: "fbdev"
	[     7.376] (II) Unloading fbdev
	[     7.376] (II) UnloadSubModule: "fbdevhw"
	[     7.376] (II) Unloading fbdevhw
	[     7.376] (II) UnloadModule: "vesa"
	[     7.376] (II) Unloading vesa
	[     7.376] (II) NVIDIA: Using 24576.00 MB of virtual memory for indirect memory
	[     7.376] (II) NVIDIA:     access.
	[     7.395] (II) NVIDIA(0): Setting mode "DFP-1:nvidia-auto-select"
	[     7.494] (==) NVIDIA(0): Disabling shared memory pixmaps
	[     7.494] (==) NVIDIA(0): Backing store enabled
	[     7.494] (==) NVIDIA(0): Silken mouse enabled
	[     7.494] (==) NVIDIA(0): DPMS enabled
	[     7.494] (II) Loading sub module "dri2"
	[     7.494] (II) LoadModule: "dri2"
	[     7.494] (II) Module "dri2" already built-in
	[     7.494] (II) NVIDIA(0): [DRI2] Setup complete
	[     7.495] (II) NVIDIA(0): [DRI2]   VDPAU driver: nvidia
	[     7.495] (II) Initializing extension Generic Event Extension
	[     7.495] (II) Initializing extension SHAPE
	[     7.495] (II) Initializing extension MIT-SHM
	[     7.495] (II) Initializing extension XInputExtension
	[     7.496] (II) Initializing extension XTEST
	[     7.496] (II) Initializing extension BIG-REQUESTS
	[     7.496] (II) Initializing extension SYNC
	[     7.496] (II) Initializing extension XKEYBOARD
	[     7.496] (II) Initializing extension XC-MISC
	[     7.496] (II) Initializing extension SECURITY
	[     7.496] (II) Initializing extension XFIXES
	[     7.496] (II) Initializing extension RENDER
	[     7.496] (II) Initializing extension RANDR
	[     7.496] (II) Initializing extension COMPOSITE
	[     7.496] (II) Initializing extension DAMAGE
	[     7.496] (II) Initializing extension MIT-SCREEN-SAVER
	[     7.496] (II) Initializing extension DOUBLE-BUFFER
	[     7.497] (II) Initializing extension RECORD
	[     7.497] (II) Initializing extension DPMS
	[     7.497] (II) Initializing extension Present
	[     7.497] (II) Initializing extension DRI3
	[     7.497] (II) Initializing extension X-Resource
	[     7.497] (II) Initializing extension XVideo
	[     7.497] (II) Initializing extension XVideo-MotionCompensation
	[     7.497] (II) Initializing extension SELinux
	[     7.497] (II) SELinux: Disabled on system
	[     7.497] (II) Initializing extension GLX
	[     7.497] (II) Initializing extension GLX
	[     7.497] (II) Indirect GLX disabled.
	[     7.497] (II) GLX: Another vendor is already registered for screen 0
	[     7.497] (II) Initializing extension XFree86-VidModeExtension
	[     7.497] (II) Initializing extension XFree86-DGA
	[     7.497] (II) Initializing extension XFree86-DRI
	[     7.497] (II) Initializing extension DRI2
	[     7.497] (II) Initializing extension NV-GLX
	[     7.497] (II) Initializing extension NV-CONTROL
	[     7.497] (II) Initializing extension XINERAMA
	[     7.525] (II) config/udev: Adding input device Power Button (/dev/input/event1)
	[     7.525] (**) Power Button: Applying InputClass "libinput keyboard catchall"
	[     7.525] (II) LoadModule: "libinput"
	[     7.526] (II) Loading /usr/lib/xorg/modules/input/libinput_drv.so
	[     7.526] (II) Module libinput: vendor="X.Org Foundation"
	[     7.527]    compiled for 1.20.4, module version = 0.29.0
	[     7.527]    Module class: X.Org XInput Driver
	[     7.527]    ABI class: X.Org XInput driver, version 24.1
	[     7.527] (II) Using input driver 'libinput' for 'Power Button'
	[     7.527] (II) systemd-logind: got fd for /dev/input/event1 13:65 fd 41 paused 0
	[     7.527] (**) Power Button: always reports core events
	[     7.527] (**) Option "Device" "/dev/input/event1"
	[     7.527] (**) Option "_source" "server/udev"
	[     7.528] (II) event1  - Power Button: is tagged by udev as: Keyboard
	[     7.528] (II) event1  - Power Button: device is a keyboard
	[     7.528] (II) event1  - Power Button: device removed
	[     7.528] (**) Option "config_info" "udev:/sys/devices/LNXSYSTM:00/LNXPWRBN:00/input/input1/event1"
	[     7.529] (II) XINPUT: Adding extended input device "Power Button" (type: KEYBOARD, id 6)
	[     7.529] (**) Option "xkb_model" "pc105"
	[     7.529] (**) Option "xkb_layout" "us"
	[     7.529] (II) event1  - Power Button: is tagged by udev as: Keyboard
	[     7.529] (II) event1  - Power Button: device is a keyboard
	[     7.529] (II) config/udev: Adding input device Power Button (/dev/input/event0)
	[     7.529] (**) Power Button: Applying InputClass "libinput keyboard catchall"
	[     7.529] (II) Using input driver 'libinput' for 'Power Button'
	[     7.530] (II) systemd-logind: got fd for /dev/input/event0 13:64 fd 44 paused 0
	[     7.530] (**) Power Button: always reports core events
	[     7.530] (**) Option "Device" "/dev/input/event0"
	[     7.530] (**) Option "_source" "server/udev"
	[     7.530] (II) event0  - Power Button: is tagged by udev as: Keyboard
	[     7.530] (II) event0  - Power Button: device is a keyboard
	[     7.531] (II) event0  - Power Button: device removed
	[     7.531] (**) Option "config_info" "udev:/sys/devices/LNXSYSTM:00/LNXSYBUS:00/PNP0C0C:00/input/input0/event0"
	[     7.531] (II) XINPUT: Adding extended input device "Power Button" (type: KEYBOARD, id 7)
	[     7.531] (**) Option "xkb_model" "pc105"
	[     7.531] (**) Option "xkb_layout" "us"
	[     7.531] (II) event0  - Power Button: is tagged by udev as: Keyboard
	[     7.531] (II) event0  - Power Button: device is a keyboard
	[     7.531] (II) config/udev: Adding input device HDA NVidia HDMI/DP,pcm=3 (/dev/input/event12)
	[     7.531] (II) No input driver specified, ignoring this device.
	[     7.531] (II) This device may have been added with another device file.
	[     7.532] (II) config/udev: Adding input device HDA NVidia HDMI/DP,pcm=7 (/dev/input/event13)
	[     7.532] (II) No input driver specified, ignoring this device.
	[     7.532] (II) This device may have been added with another device file.
	[     7.532] (II) config/udev: Adding input device HDA NVidia HDMI/DP,pcm=8 (/dev/input/event14)
	[     7.532] (II) No input driver specified, ignoring this device.
	[     7.532] (II) This device may have been added with another device file.
	[     7.532] (II) config/udev: Adding input device HDA NVidia HDMI/DP,pcm=9 (/dev/input/event15)
	[     7.532] (II) No input driver specified, ignoring this device.
	[     7.532] (II) This device may have been added with another device file.
	[     7.532] (II) config/udev: Adding input device HDA NVidia HDMI/DP,pcm=10 (/dev/input/event16)
	[     7.532] (II) No input driver specified, ignoring this device.
	[     7.532] (II) This device may have been added with another device file.
	[     7.533] (II) config/udev: Adding input device HDA NVidia HDMI/DP,pcm=11 (/dev/input/event17)
	[     7.533] (II) No input driver specified, ignoring this device.
	[     7.533] (II) This device may have been added with another device file.
	[     7.533] (II) config/udev: Adding input device HDA NVidia HDMI/DP,pcm=12 (/dev/input/event18)
	[     7.533] (II) No input driver specified, ignoring this device.
	[     7.533] (II) This device may have been added with another device file.
	[     7.533] (II) config/udev: Adding input device PixArt USB Optical Mouse (/dev/input/event2)
	[     7.533] (**) PixArt USB Optical Mouse: Applying InputClass "libinput pointer catchall"
	[     7.533] (II) Using input driver 'libinput' for 'PixArt USB Optical Mouse'
	[     7.534] (II) systemd-logind: got fd for /dev/input/event2 13:66 fd 45 paused 0
	[     7.534] (**) PixArt USB Optical Mouse: always reports core events
	[     7.534] (**) Option "Device" "/dev/input/event2"
	[     7.534] (**) Option "_source" "server/udev"
	[     7.535] (II) event2  - PixArt USB Optical Mouse: is tagged by udev as: Mouse
	[     7.535] (II) event2  - PixArt USB Optical Mouse: device is a pointer
	[     7.535] (II) event2  - PixArt USB Optical Mouse: device removed
	[     7.535] (**) Option "config_info" "udev:/sys/devices/pci0000:00/0000:00:14.0/usb3/3-3/3-3.1/3-3.1:1.0/0003:0461:4E22.0001/input/in
	put2/event2"
	[     7.535] (II) XINPUT: Adding extended input device "PixArt USB Optical Mouse" (type: MOUSE, id 8)
	[     7.535] (**) Option "AccelerationScheme" "none"
	[     7.535] (**) PixArt USB Optical Mouse: (accel) selected scheme none/0
	[     7.535] (**) PixArt USB Optical Mouse: (accel) acceleration factor: 2.000
	[     7.535] (**) PixArt USB Optical Mouse: (accel) acceleration threshold: 4
	[     7.536] (II) event2  - PixArt USB Optical Mouse: is tagged by udev as: Mouse
	[     7.536] (II) event2  - PixArt USB Optical Mouse: device is a pointer
	[     7.537] (II) config/udev: Adding input device PixArt USB Optical Mouse (/dev/input/mouse0)
	[     7.537] (II) No input driver specified, ignoring this device.
	[     7.537] (II) This device may have been added with another device file.
	[     7.537] (II) config/udev: Adding input device DELL Dell USB Entry Keyboard (/dev/input/event3)
	[     7.537] (**) DELL Dell USB Entry Keyboard: Applying InputClass "libinput keyboard catchall"
	[     7.537] (II) Using input driver 'libinput' for 'DELL Dell USB Entry Keyboard'
	[     7.538] (II) systemd-logind: got fd for /dev/input/event3 13:67 fd 46 paused 0
	[     7.538] (**) DELL Dell USB Entry Keyboard: always reports core events
	[     7.538] (**) Option "Device" "/dev/input/event3"
	[     7.538] (**) Option "_source" "server/udev"
	[     7.539] (II) event3  - DELL Dell USB Entry Keyboard: is tagged by udev as: Keyboard
	[     7.539] (II) event3  - DELL Dell USB Entry Keyboard: device is a keyboard
	[     7.539] (II) event3  - DELL Dell USB Entry Keyboard: device removed
	[     7.539] (**) Option "config_info" "udev:/sys/devices/pci0000:00/0000:00:14.0/usb3/3-3/3-3.2/3-3.2:1.0/0003:413C:2107.0002/input/in
	put3/event3"
	[     7.539] (II) XINPUT: Adding extended input device "DELL Dell USB Entry Keyboard" (type: KEYBOARD, id 9)
	[     7.539] (**) Option "xkb_model" "pc105"
	[     7.539] (**) Option "xkb_layout" "us"
	[     7.540] (II) event3  - DELL Dell USB Entry Keyboard: is tagged by udev as: Keyboard
	[     7.540] (II) event3  - DELL Dell USB Entry Keyboard: device is a keyboard
	[     7.540] (II) config/udev: Adding input device HDA Intel PCH Line Out Side (/dev/input/event10)
	[     7.540] (II) No input driver specified, ignoring this device.
	[     7.540] (II) This device may have been added with another device file.
	[     7.541] (II) config/udev: Adding input device HDA Intel PCH Front Headphone (/dev/input/event11)
	[     7.541] (II) No input driver specified, ignoring this device.
	[     7.541] (II) This device may have been added with another device file.
	[     7.541] (II) config/udev: Adding input device HDA Intel PCH Front Mic (/dev/input/event4)
	[     7.541] (II) No input driver specified, ignoring this device.
	[     7.541] (II) This device may have been added with another device file.
	[     7.541] (II) config/udev: Adding input device HDA Intel PCH Rear Mic (/dev/input/event5)
	[     7.541] (II) No input driver specified, ignoring this device.
	[     7.541] (II) This device may have been added with another device file.
	[     7.541] (II) config/udev: Adding input device HDA Intel PCH Line (/dev/input/event6)
	[     7.541] (II) No input driver specified, ignoring this device.
	[     7.541] (II) This device may have been added with another device file.
	[     7.542] (II) config/udev: Adding input device HDA Intel PCH Line Out Front (/dev/input/event7)
	[     7.542] (II) No input driver specified, ignoring this device.
	[     7.542] (II) This device may have been added with another device file.
	[     7.542] (II) config/udev: Adding input device HDA Intel PCH Line Out Surround (/dev/input/event8)
	[     7.542] (II) No input driver specified, ignoring this device.
	[     7.542] (II) This device may have been added with another device file.
	[     7.542] (II) config/udev: Adding input device HDA Intel PCH Line Out CLFE (/dev/input/event9)
	[     7.542] (II) No input driver specified, ignoring this device.
	[     7.542] (II) This device may have been added with another device file.
	[     7.546] (II) config/udev: Adding input device HDA NVidia HDMI/DP,pcm=7 (/dev/input/event13)
	[     7.546] (II) No input driver specified, ignoring this device.
	[     7.546] (II) This device may have been added with another device file.
	[     7.546] (II) config/udev: Adding input device HDA NVidia HDMI/DP,pcm=3 (/dev/input/event12)
	[     7.546] (II) No input driver specified, ignoring this device.
	[     7.546] (II) This device may have been added with another device file.
	[     7.547] (II) config/udev: Adding input device HDA NVidia HDMI/DP,pcm=9 (/dev/input/event15)
	[     7.547] (II) No input driver specified, ignoring this device.
	[     7.547] (II) This device may have been added with another device file.
	[     7.547] (II) config/udev: Adding input device HDA NVidia HDMI/DP,pcm=10 (/dev/input/event16)
	[     7.547] (II) No input driver specified, ignoring this device.
	[     7.547] (II) This device may have been added with another device file.
	[     7.547] (II) config/udev: Adding input device HDA NVidia HDMI/DP,pcm=11 (/dev/input/event17)
	[     7.547] (II) No input driver specified, ignoring this device.
	[     7.547] (II) This device may have been added with another device file.
	[     7.547] (II) config/udev: Adding input device HDA NVidia HDMI/DP,pcm=8 (/dev/input/event14)
	[     7.547] (II) No input driver specified, ignoring this device.
	[     7.547] (II) This device may have been added with another device file.
	[     7.547] (II) config/udev: Adding input device HDA NVidia HDMI/DP,pcm=12 (/dev/input/event18)
	[     7.547] (II) No input driver specified, ignoring this device.
	[     7.547] (II) This device may have been added with another device file.
	[     7.689] (--) NVIDIA(GPU-0): DFP-0: disconnected
	[     7.689] (--) NVIDIA(GPU-0): DFP-0: Internal DisplayPort
	[     7.689] (--) NVIDIA(GPU-0): DFP-0: 1440.0 MHz maximum pixel clock
	[     7.689] (--) NVIDIA(GPU-0):
	[     7.749] (--) NVIDIA(GPU-0): Samsung SMS27A850 (DFP-1): connected
	[     7.749] (--) NVIDIA(GPU-0): Samsung SMS27A850 (DFP-1): Internal TMDS
	[     7.749] (--) NVIDIA(GPU-0): Samsung SMS27A850 (DFP-1): 165.0 MHz maximum pixel clock
	[     7.749] (--) NVIDIA(GPU-0):
	[     7.749] (--) NVIDIA(GPU-0): DFP-2: disconnected
	[     7.749] (--) NVIDIA(GPU-0): DFP-2: Internal DisplayPort
	[     7.750] (--) NVIDIA(GPU-0): DFP-2: 1440.0 MHz maximum pixel clock
	[     7.750] (--) NVIDIA(GPU-0):
	[     7.750] (--) NVIDIA(GPU-0): DFP-3: disconnected
	[     7.750] (--) NVIDIA(GPU-0): DFP-3: Internal TMDS
	[     7.750] (--) NVIDIA(GPU-0): DFP-3: 165.0 MHz maximum pixel clock
	[     7.750] (--) NVIDIA(GPU-0):
	[     7.750] (--) NVIDIA(GPU-0): DFP-4: disconnected
	[     7.750] (--) NVIDIA(GPU-0): DFP-4: Internal DisplayPort
	[     7.750] (--) NVIDIA(GPU-0): DFP-4: 1440.0 MHz maximum pixel clock
	[     7.750] (--) NVIDIA(GPU-0):
	[     7.750] (--) NVIDIA(GPU-0): DFP-5: disconnected
	[     7.750] (--) NVIDIA(GPU-0): DFP-5: Internal TMDS
	[     7.750] (--) NVIDIA(GPU-0): DFP-5: 165.0 MHz maximum pixel clock
	[     7.750] (--) NVIDIA(GPU-0):
	[     7.750] (--) NVIDIA(GPU-0): DFP-6: disconnected
	[     7.750] (--) NVIDIA(GPU-0): DFP-6: Internal DisplayPort
	[     7.750] (--) NVIDIA(GPU-0): DFP-6: 1440.0 MHz maximum pixel clock
	[     7.750] (--) NVIDIA(GPU-0):
	[     7.750] (--) NVIDIA(GPU-0): DFP-7: disconnected
	[     7.750] (--) NVIDIA(GPU-0): DFP-7: Internal TMDS
	[     7.750] (--) NVIDIA(GPU-0): DFP-7: 165.0 MHz maximum pixel clock
	[     7.750] (--) NVIDIA(GPU-0):
	[     8.492] (--) NVIDIA(GPU-0): DFP-0: disconnected
	[     8.492] (--) NVIDIA(GPU-0): DFP-0: Internal DisplayPort
	[     8.492] (--) NVIDIA(GPU-0): DFP-0: 1440.0 MHz maximum pixel clock
	[     8.492] (--) NVIDIA(GPU-0):
	[     8.552] (--) NVIDIA(GPU-0): Samsung SMS27A850 (DFP-1): connected
	[     8.552] (--) NVIDIA(GPU-0): Samsung SMS27A850 (DFP-1): Internal TMDS
	[     8.552] (--) NVIDIA(GPU-0): Samsung SMS27A850 (DFP-1): 165.0 MHz maximum pixel clock
	[     8.552] (--) NVIDIA(GPU-0):
	[     8.552] (--) NVIDIA(GPU-0): DFP-2: disconnected
	[     8.552] (--) NVIDIA(GPU-0): DFP-2: Internal DisplayPort
	[     8.552] (--) NVIDIA(GPU-0): DFP-2: 1440.0 MHz maximum pixel clock
	[     8.552] (--) NVIDIA(GPU-0):
	[     8.552] (--) NVIDIA(GPU-0): DFP-3: disconnected
	[     8.552] (--) NVIDIA(GPU-0): DFP-3: Internal TMDS
	[     8.552] (--) NVIDIA(GPU-0): DFP-3: 165.0 MHz maximum pixel clock
	[     8.552] (--) NVIDIA(GPU-0):
	[     8.552] (--) NVIDIA(GPU-0): DFP-4: disconnected
	[     8.552] (--) NVIDIA(GPU-0): DFP-4: Internal DisplayPort
	[     8.552] (--) NVIDIA(GPU-0): DFP-4: 1440.0 MHz maximum pixel clock
	[     8.552] (--) NVIDIA(GPU-0):
	[     8.552] (--) NVIDIA(GPU-0): DFP-5: disconnected
	[     8.552] (--) NVIDIA(GPU-0): DFP-5: Internal TMDS
	[     8.552] (--) NVIDIA(GPU-0): DFP-5: 165.0 MHz maximum pixel clock
	[     8.552] (--) NVIDIA(GPU-0):
	[     8.552] (--) NVIDIA(GPU-0): DFP-6: disconnected
	[     8.552] (--) NVIDIA(GPU-0): DFP-6: Internal DisplayPort
	[     8.552] (--) NVIDIA(GPU-0): DFP-6: 1440.0 MHz maximum pixel clock
	[     8.552] (--) NVIDIA(GPU-0):
	[     8.553] (--) NVIDIA(GPU-0): DFP-7: disconnected
	[     8.553] (--) NVIDIA(GPU-0): DFP-7: Internal TMDS
	[     8.553] (--) NVIDIA(GPU-0): DFP-7: 165.0 MHz maximum pixel clock
	[     8.553] (--) NVIDIA(GPU-0):
	[    17.570] (**) Option "fd" "41"
	[    17.570] (II) event1  - Power Button: device removed
	[    17.570] (**) Option "fd" "44"
	[    17.570] (II) event0  - Power Button: device removed
	[    17.571] (**) Option "fd" "45"
	[    17.571] (II) event2  - PixArt USB Optical Mouse: device removed
	[    17.571] (**) Option "fd" "46"
	[    17.571] (II) event3  - DELL Dell USB Entry Keyboard: device removed
	[    17.703] (II) systemd-logind: got pause for 13:66
	[    17.703] (II) systemd-logind: got pause for 13:65
	[    17.703] (II) systemd-logind: got pause for 13:64
	[    17.703] (II) systemd-logind: got pause for 13:67
	[  4185.228] (II) UnloadModule: "libinput"
	[  4185.228] (II) systemd-logind: releasing fd for 13:67
	[  4185.246] (II) UnloadModule: "libinput"
	[  4185.246] (II) systemd-logind: releasing fd for 13:66
	[  4185.278] (II) UnloadModule: "libinput"
	[  4185.278] (II) systemd-logind: releasing fd for 13:64
	[  4185.298] (II) UnloadModule: "libinput"
	[  4185.298] (II) systemd-logind: releasing fd for 13:65
	[  4185.346] (II) NVIDIA(GPU-0): Deleting GPU-0
	[  4185.347] (WW) xf86CloseConsole: KDSETMODE failed: Input/output error
	[  4185.347] (WW) xf86CloseConsole: VT_GETMODE failed: Input/output error
	[  4185.347] (WW) xf86CloseConsole: VT_ACTIVATE failed: Input/output error
	[  4185.348] (II) Server terminated successfully (0). Closing log file.

```

```shell
	╰─○ sudo nvidia-detector
	[sudo] password for vislab:
	nvidia-driver-470
	(base) ╭─vislab at vislab-inwin in ~ 21-10-11 - 19:24:54
	╰─○ dpkg -l | grep nvidia
	ii  libnvidia-compute-460:amd64                   460.91.03-0ubuntu0.20.04.1            amd64        NVIDIA libcompute package
	rc  screen-resolution-extra                       0.18build1                            all          Extension for the nvidia-settings control panel
```

#### do resolution 2560x1440 on SyncMaster SA850
!! not a driver problem, this the DP to DVI adaptor or the DVI cable can not do more than 1080P

```shell
	## could config X server in ~/.xprofile

	## example
	# sudo xrandr --newmode "1600x900_60.00"  118.25  1600 1696 1856 2112  900 903 908 934 -hsync +vsync
	# sudo xrandr --addmode eDP-1 "1600x900_60.00"
	# sudo xrandr --newmode "2560x1440_60.00"  312.25  2560 2752 3024 3488  1440 1443 1448 1493 -hsync +vsync

	## failed
	# xrandr to get display name, DP-1
	# ╰─○ cvt 2560 1440
	# 2560x1440 59.96 Hz (CVT 3.69M9) hsync: 89.52 kHz; pclk: 312.25 MHz
	# Modeline "2560x1440_60.00"  312.25  2560 2752 3024 3488  1440 1443 1448 1493 -hsync +vsync

	## failed 02
	# gtf 2560 1440 60
	# 2560x1440 @ 60.00 Hz (GTF) hsync: 89.40 kHz; pclk: 311.83 MHz
	# Modeline "2560x1440_60.00"  311.83  2560 2744 3024 3488  1440 1441 1444 1490  -HSync +Vsync
	# sudo xrandr --newmode "test02"  311.83  2560 2744 3024 3488  1440 1441 1444 1490  -HSync +Vsync
	# sudo xrandr --addmode DP-1 "test02"

	## failed 03
	# gtf 2560 1440 30
	# 2560x1440 @ 30.00 Hz (GTF) hsync: 43.95 kHz; pclk: 146.27 MHz
	# Modeline "2560x1440_30.00"  146.27  2560 2680 2944 3328  1440 1441 1444 1465  -HSync +Vsync
	# sudo xrandr --newmode "test03" 146.27  2560 2680 2944 3328  1440 1441 1444 1465  -HSync +Vsync
	# sudo xrandr --addmode DP-1 "test03"
	# sudo xrandr --output DP-1 --mode "test03"

	# lspci -nn # to view the devices
	# check /var/log/Xorg.0.log
```

#### install mate desktop for 1440P display
from: https://linuxconfig.org/how-to-install-mate-desktop-on-ubuntu-20-04-focal-fossa-linux