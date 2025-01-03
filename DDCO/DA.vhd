library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;

entity DA is
    Port (
        x : in STD_LOGIC_VECTOR (3 downto 0);
        y : in STD_LOGIC_VECTOR (3 downto 0);
        s : out STD_LOGIC_VECTOR (4 downto 0)
    );
end DA;

architecture Behavioral of DA is
    signal Adjust : STD_LOGIC;
    signal Sum : STD_LOGIC_VECTOR (4 downto 0);
begin
    Sum <= ('0' & x) + y;  
    Adjust <= '1' when ((Sum > 9) or (Sum(4) = '1')) else '0';
    s <= Sum when (Adjust = '0') else Sum + 6;
end Behavioral;