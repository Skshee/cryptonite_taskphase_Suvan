class PasswordHexDecrypter {
    public static void main(String[] args) {
        int[] x = {1096770097, 1952395366, 1600270708, 1601398833, 1716808014, 1734291511, 960049251, 1681089078};

        byte[] hexBytes = new byte[32];

        for (int i = 0; i < 8; i++) {
            hexBytes[i * 4] = (byte) (x[i] >> 24);
            hexBytes[i * 4 + 1] = (byte) (x[i] >> 16);
            hexBytes[i * 4 + 2] = (byte) (x[i] >> 8);
            hexBytes[i * 4 + 3] = (byte) x[i];
        }
        
        for(int i=0;i<32;i++){
        System.out.println(hexBytes[i]);
        }
    }
}