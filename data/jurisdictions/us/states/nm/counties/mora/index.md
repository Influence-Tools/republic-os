---
type: Jurisdiction
title: "Mora County, NM"
classification: county
fips: "35033"
state: "NM"
demographics:
  population: 4149
  population_under_18: 710
  population_18_64: 2028
  population_65_plus: 1411
  median_household_income: 53663
  poverty_rate: 21.43
  homeownership_rate: 86.74
  unemployment_rate: 3.77
  median_home_value: 122600
  gini_index: 0.4795
  vacancy_rate: 32.67
  race_white: 1849
  race_black: 26
  race_asian: 0
  race_native: 99
  hispanic: 3049
  bachelors_plus: 1881
districts:
  - to: "us/states/nm/districts/03"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nm/districts/senate/8"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nm/districts/house/40"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Mora County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 4149 |
| Under 18 | 710 |
| 18–64 | 2028 |
| 65+ | 1411 |
| Median household income | 53663 |
| Poverty rate | 21.43 |
| Homeownership rate | 86.74 |
| Unemployment rate | 3.77 |
| Median home value | 122600 |
| Gini index | 0.4795 |
| Vacancy rate | 32.67 |
| White | 1849 |
| Black | 26 |
| Asian | 0 |
| Native | 99 |
| Hispanic/Latino | 3049 |
| Bachelor's or higher | 1881 |

## Districts

- [NM-03](/us/states/nm/districts/03.md) — 100% (congressional)
- [NM Senate District 8](/us/states/nm/districts/senate/8.md) — 100% (state senate)
- [NM House District 40](/us/states/nm/districts/house/40.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
