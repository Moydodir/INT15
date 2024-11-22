# MikroTik: Основная информация

## Ключевая информация
### Тип системы
* Программное обеспечение и оборудование для сетей.
* MikroTik производит как физические устройства (роутеры, коммутаторы и точки доступа), так и программное обеспечение для сетевого администрирования.
### Операционная система
RouterOS — это автономная операционная система на базе ядра Linux. Она поддерживает аппаратные устройства MikroTik, но также доступна для виртуальных машин.

  Разработана на основе ядра Linux.

  Основные инструменты для настройки устройств: мощный интерфейс командной строки (CLI), графический интерфейс (Winbox), а также возможность удаленного управления через веб-интерфейс и API. 
  
<u>
  ***(важно ответить, что, хотя winbox используется чаще всего, он позволяет выполнять 99% команд, в отличие от консоли. Например, при настройке Wi-Fi, такие параметры как antenna-gain увидеть не получится. Также, имеются различные неисправности, например, беспроводной интерфейс 5ГГц имеет баг во вкладке Current Tx Power, из-за чего скорости не отображаются)***
</u>

  Поддерживает широкий спектр функций: маршрутизацию, VPN, QoS, файрволы, управление трафиком и другие.

### Производитель

Компания: MikroTik.

Страна происхождения: Латвия.

Год основания: 1996.

# Описание исследуемого устройства

## Основные характеристики
Тип устройства:  hAP ac² 

Версия ROS: v7

Архитектура процессора: MIPSBE

Функции устройства: точка доступа с двойным одновременным подключением, которая обеспечивает покрытие Wi-Fi на частотах 2,4 ГГц и 5 ГГц одновременно. Пять портов Ethernet 10/100/1000 обеспечивают гигабитные подключения для проводных устройств, USB можно использовать для внешнего хранилища или модема 4G / LTE, а устройство поддерживает аппаратное ускорение IPSec.
hAP ac2 (международный) поддерживает диапазон частот 2412-2484 МГц и 5150-5875 МГц (конкретный диапазон частот может быть ограничен законодательством страны).

Полный перечень характеристик устройства можно найти по ссылке:

https://mikrotik.com/product/hap_ac2?ysclid=m3pzxz5hnd850531769

# Основные настройки устройства

## Interfaces
> Содержит основную информацию об интерфейсах. Интерфейсы могут быть Ethernet, Wireless, PPPoE, VPN, VLAN, Bridge.
```
interface/print detail 
```
```
Flags: D - dynamic; X - disabled, R - running; S - slave; P - passthrough 
 0      name="ether1" default-name="ether1" type="ether" mtu=1500 
        actual-mtu=1500 l2mtu=1598 max-l2mtu=2028 
        mac-address=64:D1:54:87:2D:1E ifname="eth0" ifindex=11 id=1 
        last-link-down-time=1970-01-05 03:29:35 
        last-link-up-time=1970-01-05 03:28:34 link-downs=1 

 1      name="ether2" default-name="ether2" type="ether" mtu=1500 
        actual-mtu=1500 l2mtu=1598 max-l2mtu=2028 
        mac-address=64:D1:54:87:2D:1F ifname="eth1" ifindex=12 id=2 
        link-downs=0 

 2   S  name="ether3" default-name="ether3" type="ether" mtu=1500 
        actual-mtu=1500 l2mtu=1598 max-l2mtu=2028 vrf=vrf2 
        mac-address=64:D1:54:87:2D:20 ifname="eth2" ifindex=13 id=3 
        link-downs=0 

 3  R   name="ether4" default-name="ether4" type="ether" mtu=1500 
        actual-mtu=1500 l2mtu=1598 max-l2mtu=2028 vrf=vrf1 
        mac-address=64:D1:54:87:2D:21 ifname="eth3" ifindex=14 id=4 
        last-link-down-time=1970-01-06 02:03:31 
        last-link-up-time=1970-01-06 02:12:30 link-downs=5 
```
## ARP
> Несмотря на то, что IP-пакеты адресуются с использованием IP-адресов, для фактической передачи данных с одного хоста на другой необходимо использовать аппаратные адреса. Протокол разрешения адресов используется для сопоставления IP-адресов OSI уровня 3 с MAC-адресами OSI уровня 2. Маршрутизатор содержит таблицу используемых в настоящее время записей ARP. Обычно таблица создается динамически, но для повышения безопасности сети ее можно частично или полностью создать статически, добавив статические записи.
Такие записи можно получить следующей коммандой
```
/ip arp print detail
```
```
Flags: X - disabled, I - invalid, H - DHCP, D - dynamic, P - published, 
C - complete 
 0 DC address=172.16.0.254 mac-address=AA:BB:CC:DD:EE:FF interface=B8-MGMT-WIFI 
      published=no 

 1 DC address=192.168.204.200 mac-address=11:22:33:44:55:66 
      interface=PUB-COMM published=no 

 2 DC address=172.16.8.252 mac-address=4C:5E:0C:02:93:71 interface=B8-MGMT-WIFI 
      published=no

```

## IP address
> Вкладка IP Address используется для управления IP-адресами, которые назначаются интерфейсам маршрутизатора.
```
ip address/print detail 
```
```
Flags: X - disabled, I - invalid, D - dynamic 
 0   address=192.168.88.1/32 network=255.255.255.0 interface=bridge1 actual-interface=bridge1 
```

## IP DHCP Client/Server
> Вкладка IP DHCP Client используется для настройки клиента DHCP, который автоматически получает IP-адрес от DHCP-сервера
> Вкладка IP DHCP Server используется для настройки сервера DHCP, который динамически выдает IP-адреса клиентам в сети.

```
ip dhcp-client print detail 
```
```
Flags: X - disabled, I - invalid, D - dynamic 
 0 I interface=ether1 add-default-route=yes default-route-distance=1 use-peer-dns=yes use-peer-ntp=yes 
     dhcp-options=hostname,clientid 

 1 I interface=ether3 add-default-route=yes default-route-distance=1 use-peer-dns=yes use-peer-ntp=yes 
     dhcp-options=hostname,clientid
```

```
ip dhcp-server print detail 
```
```
Flags: D - dynamic; X - disabled, I - invalid 
 0  I name="dhcp1" interface=Test lease-time=3d address-pool=dhcp_pool authoritative=yes use-radius=no 
      lease-script="" 
```

## IP DNS
> Вкладка IP DNS используется для настройки серверов DNS, которые маршрутизатор будет использовать для разрешения доменных имён.
```
 ip dns print
```
```                      
                      servers: 8.8.8.8,8.8.4.4
              dynamic-servers: 
               use-doh-server: 
              verify-doh-cert: no
   doh-max-server-connections: 5
   doh-max-concurrent-queries: 50
                  doh-timeout: 5s
        allow-remote-requests: no
          max-udp-packet-size: 4096
         query-server-timeout: 2s
          query-total-timeout: 10s
       max-concurrent-queries: 100
  max-concurrent-tcp-sessions: 20
                   cache-size: 2048KiB
                cache-max-ttl: 1w
      address-list-extra-time: 0s
                   cache-used: 29KiB
```
## VLAN
> В Mikrotik настройка VLAN происходит в различных вкладках, исходя из решаемых задач.
> Например, для настройки L2 VLAN (без создания VLAN интерфейсов) необходимо зайти во вкладку interface bridge vlan
```
interface/bridge/vlan/print detail 
```
```
Flags: X - disabled, D - dynamic 
 0   bridge=Test vlan-ids=20,30 tagged=ether3 untagged="" current-tagged="" current-untagged="" 
```
> Для настройки L3 VLAN (с созданием интерфейсов) а также создания маршрутизации между VLAN (Например, Router-on-a-Stick) служит вкладка interface vlan
```
interface/vlan/print detail 
```
```
Flags: X - disabled, R - running 
 0   name="VLAN2" mtu=1500 l2mtu=1594 mac-address=64:D1:54:87:2D:20 arp=enabled arp-timeout=auto 
     loop-protect=default loop-protect-status=off loop-protect-send-interval=5s loop-protect-disable-time=5m 
     vlan-id=2 interface=ether3 use-service-tag=no
```
# QoS
> Позволяет управлять приоритетами трафика и обеспечивать качество обслуживания для различных типов данных.
> простые очереди (Simple Queues) предоставляют удобный способ управления пропускной способностью и приоритетами трафика без необходимости глубокого понимания сложных концепций QoS. Простые очереди позволяют легко ограничивать скорость для определенных типов трафика и устанавливать приоритеты.
> "burst" используется в контексте управления очередями (QoS) для временного превышения установленных ограничений скорости. Это позволяет сети справляться с кратковременными всплесками трафика без значительного ухудшения качества обслуживания.

```
queue simple print detail 
```
```
Flags: X - disabled, I - invalid, D - dynamic 
 0  D name="first-simple-queue" target=172.16.0.2/32 parent=none 
      packet-marks="" priority=8/8 queue=default-small/default-small 
      limit-at=10M/10M max-limit=10M/10M burst-limit=0/0 burst-threshold=0/0 
      burst-time=0s/0s bucket-size=0.1/0.1 

 1  D name="second-simple-queue" target=10.0.0.1/32 parent=none 
      packet-marks="" priority=8/8 queue=default-small/default-small 
      limit-at=10M/10M max-limit=10M/10M burst-limit=0/0 burst-threshold=0/0 
      burst-time=0s/0s bucket-size=0.1/0.1 

 2  D name="provider" target=WIFI-Guest parent=none packet-marks="" 
      priority=8/8 queue=hotspot-default/hotspot-default limit-at=0/0 
      max-limit=0/0 burst-limit=0/0 burst-threshold=0/0 burst-time=0s/0s 
      bucket-size=0.1/0.1 
```

# Маршрутизация
> Здесь приведены примеры настроек OSPF и BGP. Более полную информацию о возможных настройках протоколов маршрутизации можно найти по ссылке:

https://help.mikrotik.com/docs/spaces/ROS/pages/328222/Routing

## IP Routes
> Вкладка IP Routes используется для настройки маршрутизации, чтобы управлять тем, как маршрутизатор отправляет пакеты данных в другие сети. Имеется возможность добавления статических маршрутов, указания шлюзов и приоритетов для различных маршрутов.
```
ip route print detail 
```
```
Flags: X - disabled, A - active, D - dynamic, 
C - connect, S - static, r - rip, b - bgp, o - ospf, m - mme, 
B - blackhole, U - unreachable, P - prohibit
 0 A S  dst-address=0.0.0.0/0 gateway=172.16.0.254 
        gateway-status=172.16.0.254 on VRF-MGMT-NET reachable via  vlan3 
        distance=1 scope=30 target-scope=10 routing-mark=VRF-MGMT-NET 

 1 ADC  dst-address=172.30.8.0/24 pref-src=172.16.0.130 gateway=vlan3 
        gateway-status=vlan3 reachable distance=0 scope=10 
        routing-mark=VRF-MGMT-NET 

 2 A S  dst-address=0.0.0.0/0 gateway=10.0.0.97 
        gateway-status=10.0.0.97 reachable via  ISP distance=1 
        scope=30 target-scope=10 

 3 ADC  dst-address=192.168.1.0/29 pref-src=192.168.1.8 gateway=vlan131 
        gateway-status=vlan131 reachable distance=0 scope=10 
```

## Routing BGP
> используется для управления и конфигурации различных аспектов BGP-маршрутизации:
> Инстансы (Instances), соседи (Peers), маршруты (Routes), политики (Policies), атрибуты маршрутов (Route Attributes), мониторинг, диагностика и безопасность

```
routing bgp instance print detail 
```
```
Flags: * - default, X - disabled 
 0 *  name="default" as=65530 router-id=0.0.0.0 redistribute-connected=no 
      redistribute-static=no redistribute-rip=no redistribute-ospf=no 
      redistribute-other-bgp=no out-filter="" client-to-client-reflection=yes 
      ignore-as-path-len=no routing-table="
```

## Routing OSPF
>используется для настройки и управления протоколом OSPF (Open Shortest Path First), который является одним из наиболее распространенных протоколов маршрутизации в IP-сетях. OSPF используется для динамической маршрутизации внутри автономных систем (AS).

Просмотр OSPF-инстансов:
```
 routing ospf instance print detail 
```
```
Flags: X - disabled, * - default 
 0  * name="default" router-id=172.16.0.24 distribute-default=never 
      redistribute-connected=no redistribute-static=no redistribute-rip=no 
      redistribute-bgp=no redistribute-other-ospf=no metric-default=10 
      metric-connected=20 metric-static=20 metric-rip=20 metric-bgp=auto 
      metric-other-ospf=auto in-filter=ospf-in out-filter=ospf-out 
```

Просмотр OSPF-интерфейсов:
```
routing ospf interface print detail 
```
```
Flags: X - disabled, I - inactive, D - dynamic, P - passive 
 0    interface=B3-RING cost=10 priority=125 authentication=none 
      authentication-key="" authentication-key-id=1 network-type=default 
      instance-id=0 retransmit-interval=5s transmit-delay=1s 
      hello-interval=10s dead-interval=40s use-bfd=no 

 1    interface=gre-tunnel1 cost=10 priority=1 authentication=none 
      authentication-key="" authentication-key-id=0 
      network-type=point-to-point instance-id=0 retransmit-interval=5s 
      transmit-delay=1s hello-interval=10s dead-interval=40s use-bfd=no 

 2    interface=gre-tunnel2 cost=10 priority=0 authentication=none 
      authentication-key="" authentication-key-id=1 
      network-type=point-to-point instance-id=0 retransmit-interval=5s 
      transmit-delay=1s hello-interval=10s dead-interval=40s use-bfd=no 
```
Просмотр OSPF-соседей:
```
 routing ospf neighbor print detail 
```
```
0 instance=default router-id=172.16.0.25 address=172.16.0.25 
   interface=gre-tunnel1 priority=1 dr-address=0.0.0.0 
   backup-dr-address=0.0.0.0 state="Full" state-changes=82 ls-retransmits=0 
   ls-requests=0 db-summaries=0 adjacency=10m20s 

 1 instance=default router-id=172.16.0.26 address=10.0.0.1 
   interface=gre-tunnel2 priority=0 dr-address=0.0.0.0 
   backup-dr-address=0.0.0.0 state="Full" state-changes=4 ls-retransmits=0 
   ls-requests=0 db-summaries=0 adjacency=5w3d22h25m43s 
```
Просмотр OSPF-маршрутов:
```
 routing ospf route print detail 
```
```
0 instance=default dst-address=0.0.0.0/0 state=ext-2 gateway=172.16.0.208 
   interface=gre-tunnel1 cost=10 area=external 

 1 instance=default dst-address=10.0.32.0/29 state=inter-area 
   gateway=172.16.0.208 interface=gre-tunnel1 cost=21 area=backbone 

 2 instance=default dst-address=10.0.32.16/28 state=inter-area 
   gateway=172.16.0.208 interface=gre-tunnel1 cost=21 area=backbone 

 3 instance=default dst-address=10.0.32.112/28 state=inter-area 
   gateway=172.16.0.208 interface=gre-tunnel1 cost=21 area=backbone
```
## VRF
> RouterOS позволяет создавать несколько экземпляров виртуальной маршрутизации и пересылки на одном маршрутизаторе. Это полезно для VPN MPLS на основе BGP. В отличие от BGP VPLS, которая является технологией уровня 2 OSI, VPN BGP VRF работают на уровне 3 и как таковые обмениваются IP-префиксами между маршрутизаторами. VRF решают проблему перекрытия IP-префиксов и обеспечивают необходимую конфиденциальность (посредством раздельной маршрутизации для разных VPN).

Имеющиеся VRF можно получить командой:
```
/ip vrf print detail
```
```
Flags: X - disabled; * - builtin 
 0    ;;; Another custom VRF
      name="vrf2" interfaces=bridge1 

 1    ;;; Custom VRF
      name="vrf1" interfaces=ether3,ether4 

 2  * name="main" interfaces=all
```


# Wi-Fi
> Настройка Wi-Fi в MikroTik RouterOS может быть выполнена как вручную, так и с использованием CAPsMAN (Controlled Access Point System Manager). В этом разделе описывается вывод информации о беспроводных протоколах 802.11.
> Более полная информация здесь:
https://help.mikrotik.com/docs/spaces/ROS/pages/1409138/Wireless

```
interface wireless print detail advanced 
```
данная команда может содержать весьма объёмный вывод ввиду большого количества возможных настроек бнспроводных интерфейсов: режима, стандарта(например, есть возможность не использовать старые стандарты типа 802.11b, 802.11g ввиду безопасности и исключения случаев подключения к сети за пределами контролируемой зоны), частоты, профилей безопасности, страны, WPS, различных флагов(типа Hide SSID), скоростей(VHT MCS, HT, HT MCS), VLAN, Tx Limit, возможность пропускать каналы DFS и др.
```
Flags: X - disabled, R - running 
 0    ;;; WIFI | 2.4GHz
      name="wlan1" mtu=1500 l2mtu=1600 mac-address=74:4D:28:63:21:2A 
      arp=enabled disable-running-check=no interface-type=IPQ4019 
      radio-name="744D2863212A" mode=ap-bridge ssid="MY-SSID" area="" 
      frequency-mode=manual-txpower country=russia3 installation=indoor 
      antenna-gain=6 frequency=2427 band=2ghz-onlyn channel-width=20mhz 
      secondary-frequency="" scan-list=default wireless-protocol=802.11 
      rate-set=configured supported-rates-b="" 
      supported-rates-a/g=9Mbps,12Mbps,18Mbps,24Mbps,36Mbps,48Mbps,54Mbps 
      basic-rates-b="" basic-rates-a/g=9Mbps max-station-count=32 
      distance=indoors tx-power=11 tx-power-mode=all-rates-fixed 
      vlan-mode=use-tag vlan-id=256 wds-mode=disabled wds-default-bridge=none 
      wds-default-cost=100 wds-cost-range=50-150 wds-ignore-ssid=no 
      update-stats-interval=disabled bridge-mode=enabled 
      default-authentication=yes default-forwarding=yes default-ap-tx-limit=0 
      default-client-tx-limit=0 wmm-support=enabled hide-ssid=no 
      security-profile=WIFI wps-mode=disabled 
      station-roaming=disabled disconnect-timeout=3s on-fail-retry-time=100ms 
      preamble-mode=both compression=no allow-sharedkey=no 
      station-bridge-clone-mac=00:00:00:00:00:00 ampdu-priorities=0 
      guard-interval=any 
      ht-supported-mcs=mcs-0,mcs-1,mcs-2,mcs-3,mcs-4,mcs-5,mcs-6,mcs-7,mcs-8,
                 mcs-9,mcs-10,mcs-11,mcs-12,mcs-13,mcs-14,mcs-15,mcs-16,mcs-17,
                 mcs-18,mcs-19,mcs-20,mcs-21,mcs-22,mcs-23 
      ht-basic-mcs=mcs-0,mcs-1,mcs-2,mcs-3,mcs-4,mcs-5,mcs-6,mcs-7 
      tx-chains=0,1 rx-chains=0,1 amsdu-limit=8192 amsdu-threshold=8192 
      tdma-period-size=2 nv2-queue-count=2 nv2-qos=default nv2-cell-radius=30 
      nv2-security=disabled nv2-preshared-key="" nv2-mode=dynamic-downlink 
      nv2-downlink-ratio=50 nv2-sync-secret="" hw-retries=7 frame-lifetime=0 
      adaptive-noise-immunity=none hw-fragmentation-threshold=disabled 
      hw-protection-mode=none hw-protection-threshold=0 frequency-offset=0 
      rate-selection=advanced multicast-helper=full 
      multicast-buffering=enabled keepalive-frames=enabled 
      skip-dfs-channels=disabled 

 1    ;;; WIFI | 5 GHz
      name="wlan2" mtu=1500 l2mtu=1600 mac-address=74:4D:28:63:21:2B 
      arp=enabled disable-running-check=no interface-type=IPQ4019 
      radio-name="744D2863212B" mode=ap-bridge ssid="MY-SSID-5" area="" 
      frequency-mode=manual-txpower country=russia3 installation=indoor 
      antenna-gain=6 frequency=5240 band=5ghz-n/ac channel-width=20mhz 
      secondary-frequency="" scan-list=default wireless-protocol=802.11 
      rate-set=configured 
      supported-rates-a/g=9Mbps,12Mbps,18Mbps,24Mbps,36Mbps,48Mbps,54Mbps 
      basic-rates-a/g=9Mbps max-station-count=32 distance=indoors tx-power=14 
      tx-power-mode=all-rates-fixed vlan-mode=use-tag vlan-id=256 
      wds-mode=disabled wds-default-bridge=none wds-default-cost=100 
      wds-cost-range=50-150 wds-ignore-ssid=no update-stats-interval=disabled 
      bridge-mode=enabled default-authentication=yes default-forwarding=yes 
      default-ap-tx-limit=0 default-client-tx-limit=0 wmm-support=enabled 
      hide-ssid=no security-profile=WIFI wps-mode=disabled 
      station-roaming=disabled disconnect-timeout=3s on-fail-retry-time=100ms 
      preamble-mode=both compression=no allow-sharedkey=no 
      station-bridge-clone-mac=00:00:00:00:00:00 ampdu-priorities=0 
      guard-interval=any 
      ht-supported-mcs=mcs-0,mcs-1,mcs-2,mcs-3,mcs-4,mcs-5,mcs-6,mcs-7,mcs-8,
                 mcs-9,mcs-10,mcs-11,mcs-12,mcs-13,mcs-14,mcs-15,mcs-16,mcs-17,
                 mcs-18,mcs-19,mcs-20,mcs-21,mcs-22,mcs-23 
      ht-basic-mcs=mcs-0,mcs-1,mcs-2,mcs-3,mcs-4,mcs-5,mcs-6,mcs-7 
      vht-supported-mcs=mcs0-9 vht-basic-mcs=mcs0-7 tx-chains=0,1 
      rx-chains=0,1 amsdu-limit=8192 amsdu-threshold=8192 tdma-period-size=2 
      nv2-queue-count=2 nv2-qos=default nv2-cell-radius=30 
      nv2-security=disabled nv2-preshared-key="" nv2-mode=dynamic-downlink 
      nv2-downlink-ratio=50 nv2-sync-secret="" hw-retries=7 frame-lifetime=0 
      adaptive-noise-immunity=none hw-fragmentation-threshold=disabled 
      hw-protection-mode=none hw-protection-threshold=0 frequency-offset=0 
      rate-selection=advanced multicast-helper=full 
      multicast-buffering=enabled keepalive-frames=enabled 
      skip-dfs-channels=disabled 
```
ACL Wi-Fi можно получить следующей командой:
```
interface wireless access-list print detail 
```
```
Flags: X - disabled 
 0   mac-address=00:00:00:00:00:00 interface=any signal-range=-75..120 allow-signal-out-of-range=10s 
     authentication=yes forwarding=no ap-tx-limit=0 client-tx-limit=0 private-algo=none private-key="" 
     private-pre-shared-key="" management-protection-key="" vlan-mode=default vlan-id=1 

 1   mac-address=00:00:00:00:00:00 interface=any signal-range=-120..-75 allow-signal-out-of-range=10s 
     authentication=no forwarding=no ap-tx-limit=0 client-tx-limit=0 private-algo=none private-key="" 
     private-pre-shared-key="" management-protection-key="" vlan-mode=default vlan-id=1 
```
Для вывода настроек профилей безопасности введите следующую команду
```
interface wireless security-profiles print detail
```
```
Flags: * - default 
 0 * name="default" mode=none authentication-types="" unicast-ciphers=aes-ccm group-ciphers=aes-ccm 
     wpa-pre-shared-key="" wpa2-pre-shared-key="" supplicant-identity="MikroTik" eap-methods=passthrough 
     tls-mode=no-certificates tls-certificate=none mschapv2-username="" mschapv2-password="" disable-pmkid=no 
     static-algo-0=none static-key-0="" static-algo-1=none static-key-1="" static-algo-2=none static-key-2="" 
     static-algo-3=none static-key-3="" static-transmit-key=key-0 static-sta-private-algo=none 
     static-sta-private-key="" radius-mac-authentication=no radius-mac-accounting=no radius-eap-accounting=no 
     interim-update=0s radius-mac-format=XX:XX:XX:XX:XX:XX radius-mac-mode=as-username 
     radius-called-format=mac:ssid radius-mac-caching=disabled group-key-update=5m management-protection=disabled 
     management-protection-key="" 

 1   name="WIFI" mode=dynamic-keys authentication-types=wpa2-psk unicast-ciphers=aes-ccm 
     group-ciphers=aes-ccm wpa-pre-shared-key="" wpa2-pre-shared-key="123qwerty" supplicant-identity="" 
     eap-methods="" tls-mode=no-certificates tls-certificate=none mschapv2-username="" mschapv2-password="" 
     disable-pmkid=no static-algo-0=none static-key-0="" static-algo-1=none static-key-1="" static-algo-2=none 
     static-key-2="" static-algo-3=none static-key-3="" static-transmit-key=key-0 static-sta-private-algo=none 
     static-sta-private-key="" radius-mac-authentication=no radius-mac-accounting=no radius-eap-accounting=no 
     interim-update=0s radius-mac-format=XX:XX:XX:XX:XX:XX radius-mac-mode=as-username 
     radius-called-format=mac:ssid radius-mac-caching=disabled group-key-update=5m management-protection=disabled 
     management-protection-key=""
```
# Настройки безопасности

## ACL
> это список контроля доступом, с помощью которого для субъектов (чаще всего пользователей) устанавливаются допустимые операции с объектом. В Mikrotik ACL могут настраиваться в разных частях системы и служат для разных задач.

### 1. IP Services

   Контролирует доступ к службам маршрутизатора (Winbox, SSH, Telnet, API и др.).

   Можно получить следующей командой:
```
   /ip service print
```
```
  
Flags: X - disabled, I - invalid 
 #   NAME     PORT ADDRESS                                        CERTIFICATE   
 0 XI telnet     23
 1 XI ftp        21
 2 XI www        80
 3   ssh        22 192.168.0.192/27                              
                   10.0.240.0/28                                 
 4 XI www-ssl   443                                                none          
 5 XI api      8728
 6   winbox   8291 192.168.0.192/27                              
                   10.0.240.0/28                                 
 7 XI api-ssl  8729                                                none       
```

### 2. Bridge Filters
> Позволяет контролировать трафик, проходящий между интерфейсами, связанными через мост (Bridge).
```
interface bridge filter print
```
```
Flags: X - disabled, I - invalid, D - dynamic 
 0   chain=forward action=drop in-interface=ether3 log=no log-prefix="" 

 1   chain=forward action=drop mac-protocol=arp
```

## Firewall

> Понимание потока пакетов. Такие задачи, такие как приоритизация и фильтрация трафика, политики маршрутизации, когда необходимо использовать более ?одного средства RouterOS, требуют знаний: как эти средства работают вместе? Что происходит, когда и почему?
>
> Схема потока пакетов RouterOS и примеры потоков попытаются ответить на эти вопросы.
>
>  Было бы очень сложно представить, что происходит с пакетом, на одной диаграмме, поэтому схема потока передачи пакетов разделена на три части:
>
> общая схема;
подробная схема подключения, маршрутизации и MPLS;
диаграмма, показывающая, какие средства и в каком порядке включены в предварительную маршрутизацию, ввод, пересылку, вывод и последующую маршрутизацию.

Общая схема выглядит следующим образом:
![image](https://github.com/user-attachments/assets/7a39396c-0bc6-4c93-982a-f8da685e21b3)

Полное описание Packetflow Diagram можно найти по ссылке:
https://help.mikrotik.com/docs/spaces/ROS/pages/328227/Packet+Flow+in+RouterOS

Для настройки Firewall в Mikrotik служит страница IP Firewall

IP Firewall включает в себя множество вкладок:
### 1. Filter Rules
> предназначена для управления правилами фильтрации трафика. С ее помощью можно настроить контроль за входящим, исходящим и транзитным трафиком
```
 ip firewall/filter/print cetail
```
```
Flags: X - disabled, I - invalid; D - dynamic 
 0  D ;;; special dummy rule to show fasttrack counters
      chain=forward action=passthrough 

 1    chain=output action=drop protocol=icmp src-address=10.0.0.1 
      out-interface=ether3 log=no log-prefix="" 

 2    chain=input action=fasttrack-connection hw-offload=yes protocol=udp 
      src-address=172.16.0.32 packet-mark=TV dscp=56 log=no log-prefix="" 
```
### 2. NAT
> используется для настройки преобразования сетевых адресов. NAT позволяет изменять IP-адреса и порты в заголовках пакетов при их прохождении через маршрутизатор.
``` 
 ip firewall/nat/print detail                                  
```
```
Flags: X - disabled, I - invalid; D - dynamic                         
 0    chain=dstnat action=dst-nat to-addresses=192.168.1.100 to-ports=80 
      protocol=tcp dst-address=1.2.3.4 dst-port=80 

 1    chain=srcnat action=src-nat to-addresses=1.2.3.4 src-address=192.168.1.50 
```
### 3. Mangle
> Предназначена для маркировки трафика. Она позволяет устанавливать метки для пакетов, соединений или маршрутов, чтобы они могли быть обработаны особым образом в других подсистемах маршрутизатора, таких как QoS (очереди), маршрутизация или NAT.
```
 ip firewall mangle print detail                              
```
```
Flags: X - disabled, I - invalid; D - dynamic               
 0  D ;;; special dummy rule to show fasttrack counters
      chain=prerouting action=passthrough 

 1  D ;;; special dummy rule to show fasttrack counters
      chain=forward action=passthrough 

 2  D ;;; special dummy rule to show fasttrack counters
      chain=postrouting action=passthrough 

 3    chain=prerouting action=mark-packet new-packet-mark=voip passthrough=no 
      protocol=udp dst-port=5060 
```
### Raw
> Предназначена для первичной обработки пакетов на уровне сетевого стека. Она позволяет выполнять базовую фильтрацию трафика до других обработок, таких как NAT, Mangle или Filter. Это обеспечивает более высокую производительность и гибкость, так как фильтрация в Raw снижает нагрузку на процессор маршрутизатора.

```
ip firewall raw print detail
```
```
Flags: X - disabled, I - invalid; D - dynamic 
 0  D ;;; special dummy rule to show fasttrack counters
      chain=prerouting action=passthrough 

 1    chain=prerouting action=drop src-address-list=port_scanners
```
### Service Ports
> используется для управления предопределёнными сервисами, которые маршрутизатор обрабатывает на уровне ядра. Эти сервисы включают специфичные протоколы, такие как FTP, SIP, GRE, PPTP, и многие другие, которые требуют особой обработки для корректной работы.
```
 /ip firewall service-port print detail
```
```
Flags: X - disabled, I - invalid 
 0   name="ftp" ports=21 

 1   name="tftp" ports=69 

 2 X name="irc" ports=6667 

 3   name="h323" 

 4   name="sip" ports=5060,5061 sip-direct-media=yes sip-timeout=1h 

 5   name="pptp" 

 6 X name="rtsp" ports=554 

 7   name="udplite" 

 8   name="dccp" 

 9   name="sctp" 
```
### Address Lists
> Address Lists — это списки IP-адресов, которые используются в правилах Firewall. Они помогают упростить и автоматизировать управление доступом к сети.
```
ip firewall address-list print detail
```
```
Columns: LIST, ADDRESS, CREATION-TIME
# LIST           ADDRESS        CREATION-TIME      
0 port_scanners  192.168.1.100  1970-01-06 02:22:35
```
### Layer 7 Protocols
> позволяет идентифицировать трафик на основе анализа содержимого пакетов. Он используется для управления приложениями или сервисами, которые работают поверх TCP/UDP.
```
ip firewall layer7-protocol print detail 
```
```
 0 name="youtube" regexp="^.*(youtube\.com|ytimg\.com).*$" 
```

# RADIUS
> RADIUS, сокращение от Remote Authentication Dial-In User Service, представляет собой удаленный сервер, который обеспечивает средства аутентификации и учета для различных сетевых устройств. Аутентификация и учет RADIUS позволяют интернет-провайдеру или сетевому администратору управлять доступом и учетом пользователей PPP с одного сервера в большой сети. MikroTik RouterOS имеет RADIUS-клиент, который может аутентифицировать локальных пользователей маршрутизатора, соединения HotSpot, PPP, PPPoE, PPTP, L2TP, OVPN, SSTP, IPsec и ISDN. Атрибуты, полученные от RADIUS-сервера, переопределяют атрибуты, установленные в профиле по умолчанию, но если некоторые параметры не получены, они берутся из соответствующего профиля по умолчанию. К базе данных сервера RADIUS обращаются только в том случае, если в локальной базе данных маршрутизатора не найдена соответствующая запись о доступе пользователя. Если учет RADIUS включен, учетная информация также отправляется на сервер RADIUS по умолчанию для этой службы.
>
> ссылка на документацию: https://help.mikrotik.com/docs/spaces/ROS/pages/328097/RADIUS

```
 radius print detail 
```
```
Flags: X - disabled 
 0   service=my-service called-id="" domain="" address=195.200.11.110 
     secret="some_secret" authentication-port=1812 accounting-port=1813 
     timeout=3s accounting-backup=no realm="" protocol=udp certificate=none
```

# SNMP
> Простой протокол управления сетью (SNMP) — это стандартный Интернет-протокол для управления устройствами в IP-сетях. SNMP можно использовать для графического отображения различных данных с помощью таких инструментов, как CACTI, MRTG или The Dude. Поддержка записи SNMP доступна только для некоторых OID. Для поддерживаемых OID поддерживается запись SNMP v1, v2 или v3.
>
> ссылка на документацию: https://help.mikrotik.com/docs/spaces/ROS/pages/8978519/SNMP

Для вывода глобальных настроек используется команда:
```
snmp print 
```
```
          enabled: yes
          contact: 
         location: 
        engine-id: 
      trap-target: 
   trap-community: device
     trap-version: 3
  trap-generators: temp-exception
```
Для установки прав доступа к данным SNMP используется вкладка SNMP Communities. В версиях v1 и v2c мало безопасности, только строка сообщества в виде открытого текста («имя пользователя») и возможность ограничения доступа по IP-адресу. В производственной среде следует использовать SNMP v3, поскольку он обеспечивает безопасность — авторизация (пользователь + пароль) с MD5/SHA1, шифрование с помощью DES и AES).
```
snmp community print detail 
```
```
Flags: * - default, X - disabled 
 0 *  name="public" addresses=::/0 security=none read-access=yes write-access=no 
      authentication-protocol=MD5 encryption-protocol=DES 
      authentication-password="" encryption-password="" 

 1    name="device" addresses=192.168.3.0/24 security=private read-access=yes 
      write-access=no authentication-protocol=SHA1 encryption-protocol=AES 
      authentication-password="87654321" 
      encryption-password="12345678" 
```
## Полезные ссылки
https://help.mikrotik.com/docs/
https://wiki.mikrotik.com/Manual:IP/Firewall
