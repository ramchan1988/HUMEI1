
import bencode
import hashlib
from urllib.parse import quote


def torrent_file_to_magnet(torrent_file):
    data = open(torrent_file, 'rb').read()
    metadata = bencode.bdecode(data)
    name = metadata['info']['name']
    dn = quote(name)
    info_bts = bencode.bencode(metadata['info'])
    info_hash = hashlib.sha1(info_bts).hexdigest()
    return f'magnet:?xt=urn:btih:{info_hash}&dn={dn}'


if __name__ == '__main__':
    torrent_file ='E:/HUMEI/bolck_link_name_2.npy'
    print(torrent_file_to_magnet(torrent_file))
