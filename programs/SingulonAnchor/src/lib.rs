use anchor_lang::prelude::*;

declare_id!("YourProgramIDHere12345ABCDE");

#[program]
pub mod singulon_anchor {
    use super::*;

    pub fn initialize(ctx: Context<Initialize>) -> Result<()> {
        msg!("Singulon Anchor program initialized.");
        Ok(())
    }

    pub fn update_equilibrium(ctx: Context<UpdateEquilibrium>, new_balance: u64) -> Result<()> {
        msg!("Equilibrium updated to {}", new_balance);
        let eq_account = &mut ctx.accounts.equilibrium_account;
        eq_account.balance = new_balance;
        Ok(())
    }
}

#[derive(Accounts)]
pub struct Initialize<'info> {
    #[account(init, payer = user, space = 8 + 8)]
    pub equilibrium_account: Account<'info, EquilibriumAccount>,
    #[account(mut)]
    pub user: Signer<'info>,
    pub system_program: Program<'info, System>,
}

#[derive(Accounts)]
pub struct UpdateEquilibrium<'info> {
    #[account(mut)]
    pub equilibrium_account: Account<'info, EquilibriumAccount>,
}

#[account]
pub struct EquilibriumAccount {
    pub balance: u64,
}
