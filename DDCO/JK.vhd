library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity JK is
    Port ( J : in  STD_LOGIC;
           K : in  STD_LOGIC;
           clk : in  STD_LOGIC;
           Q : out  STD_LOGIC;
           Qn : out  STD_LOGIC);
end JK;

architecture Behavioral of JK is
begin
    process(clk)
        variable temp: STD_LOGIC := '0';
    begin
        if rising_edge(clk) then
            if (J = '0' and K = '0') then temp := temp;
            elsif (J = '0' and K = '1') then temp := '0';
            elsif (J = '1' and K = '0') then temp := '1';
            else temp := not temp;
            end if;
        end if;
        Q <= temp;
        Qn <= not temp;
    end process;
end Behavioral;
