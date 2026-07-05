---
type: Jurisdiction
title: "Henderson County, NC"
classification: county
fips: "37089"
state: "NC"
demographics:
  population: 118484
  population_under_18: 22143
  population_18_64: 64965
  population_65_plus: 31376
  median_household_income: 68187
  poverty_rate: 11.56
  homeownership_rate: 75.02
  unemployment_rate: 3.46
  median_home_value: 351400
  gini_index: 0.4496
  vacancy_rate: 12.02
  race_white: 96573
  race_black: 3434
  race_asian: 1444
  race_native: 1524
  hispanic: 15507
  bachelors_plus: 44465
districts:
  - to: "us/states/nc/districts/11"
    rel: in-district
    area_weight: 0.9978
  - to: "us/states/nc/districts/senate/48"
    rel: in-district
    area_weight: 0.9988
  - to: "us/states/nc/districts/house/117"
    rel: in-district
    area_weight: 0.6671
  - to: "us/states/nc/districts/house/113"
    rel: in-district
    area_weight: 0.3317
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nc]
timestamp: "2026-07-03"
---

# Henderson County, NC

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 118484 |
| Under 18 | 22143 |
| 18–64 | 64965 |
| 65+ | 31376 |
| Median household income | 68187 |
| Poverty rate | 11.56 |
| Homeownership rate | 75.02 |
| Unemployment rate | 3.46 |
| Median home value | 351400 |
| Gini index | 0.4496 |
| Vacancy rate | 12.02 |
| White | 96573 |
| Black | 3434 |
| Asian | 1444 |
| Native | 1524 |
| Hispanic/Latino | 15507 |
| Bachelor's or higher | 44465 |

## Districts

- [NC-11](/us/states/nc/districts/11.md) — 100% (congressional)
- [NC Senate District 48](/us/states/nc/districts/senate/48.md) — 100% (state senate)
- [NC House District 117](/us/states/nc/districts/house/117.md) — 67% (state house)
- [NC House District 113](/us/states/nc/districts/house/113.md) — 33% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
