library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity SR is
    Port (
        S   : in  STD_LOGIC;
        R   : in  STD_LOGIC;
        clk : in  STD_LOGIC;
        Q   : out STD_LOGIC;
        Qn  : out STD_LOGIC
    );
end SR;

architecture Behavioral of SR is
begin
    process(clk)
        variable temp : STD_LOGIC := '0';
    begin
        if rising_edge(clk) then
            if (S = '0' and R = '0') then temp := temp;
            elsif (S = '0' and R = '1') then temp := '0';
            elsif (S = '1' and R = '0') then temp := '1';
            else temp := '0';
            end if;
        end if;
        Q <= temp;
        Qn <= not temp;
    end process;
end Behavioral;
