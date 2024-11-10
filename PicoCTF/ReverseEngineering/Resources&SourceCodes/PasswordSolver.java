class PasswordSolver {
    public static void main(String[] args) {
        String s = "jU5t_a_sna_3lpm18g947_u_4_m9r54f";
        char[] password = new char[32];
        
        
        for(int i = 0; i < 8; i++) {
            password[i] = s.charAt(i);
        }
        
        
        for(int i = 8; i < 16; i++) {
            password[23-i] = s.charAt(i);
        }
        
        
        for(int i = 16; i < 32; i += 2) {
            password[46-i] = s.charAt(i);
        }
        
        
        for(int i = 31; i >= 17; i -= 2) {
            password[i] = s.charAt(i);
        }
        password.toString();
        System.out.println(password);
    }
}