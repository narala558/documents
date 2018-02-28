// Android

// permissions



// bluetooth

// get device by macaddress
String macAddress = "98:D3:34:90:B2:E3";
BluetoothDevice device = mBluetoothAdapter.getRemoteDevice(macAddress);

// get device by name
String deviceName = "HC-05";
Set<BluetoothDevice> devices = mBluetoothAdapter.getBondedDevices();
if (devices != null) {
    for (BluetoothDevice device : devices) {
        if (deviceName.equals(device.getName())) {
            btDevice = device;
            break;
        }
    }
}
