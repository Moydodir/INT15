# MikroTik: Основная информация

## Ключевая информация
### Тип системы
* Программное обеспечение и оборудование для сетей.
* MikroTik производит как физические устройства (роутеры, коммутаторы и точки доступа), так и программное обеспечение для сетевого администрирования.
### Операционная система
RouterOS — это автономная операционная система на базе ядра Linux. Она поддерживает аппаратные устройства MikroTik, но также доступна для виртуальных машин.

  Разработана на основе ядра Linux.

  Основные инструменты для настройки устройств: мощный интерфейс командной строки (CLI), графический интерфейс (Winbox), а также возможность удаленного управления через веб-интерфейс и API. 
  
  ***(важно ответить, что, хотя winbox используется чаще всего, он позволяет выполнять 99% команд, в отличие от консоли. Например, при настройке Wi-Fi, такие параметры как antenna-gain увидеть не получится. Также, имеются различные неисправности, например, беспроводной интерфейс 5ГГц имеет баг во вкладке Current Tx Power, из-за чего скорости не отображаются)***
  
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

## Полезные ссылки
https://help.mikrotik.com/docs/
https://wiki.mikrotik.com/Manual:IP/Firewall
