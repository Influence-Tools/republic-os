---
type: Jurisdiction
title: "Paulding County, GA"
classification: county
fips: "13223"
state: "GA"
demographics:
  population: 178909
  population_under_18: 45577
  population_18_64: 112335
  population_65_plus: 20997
  median_household_income: 98031
  poverty_rate: 6.65
  homeownership_rate: 80.77
  unemployment_rate: 4.51
  median_home_value: 326300
  gini_index: 0.3589
  vacancy_rate: 4.93
  race_white: 111895
  race_black: 41833
  race_asian: 2627
  race_native: 529
  hispanic: 15643
  bachelors_plus: 46638
districts:
  - to: "us/states/ga/districts/14"
    rel: in-district
    area_weight: 0.9985
  - to: "us/states/ga/districts/senate/31"
    rel: in-district
    area_weight: 0.8451
  - to: "us/states/ga/districts/senate/30"
    rel: in-district
    area_weight: 0.1548
  - to: "us/states/ga/districts/house/17"
    rel: in-district
    area_weight: 0.3565
  - to: "us/states/ga/districts/house/16"
    rel: in-district
    area_weight: 0.2208
  - to: "us/states/ga/districts/house/19"
    rel: in-district
    area_weight: 0.1517
  - to: "us/states/ga/districts/house/18"
    rel: in-district
    area_weight: 0.1438
  - to: "us/states/ga/districts/house/40"
    rel: in-district
    area_weight: 0.1271
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ga]
timestamp: "2026-07-03"
---

# Paulding County, GA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 178909 |
| Under 18 | 45577 |
| 18–64 | 112335 |
| 65+ | 20997 |
| Median household income | 98031 |
| Poverty rate | 6.65 |
| Homeownership rate | 80.77 |
| Unemployment rate | 4.51 |
| Median home value | 326300 |
| Gini index | 0.3589 |
| Vacancy rate | 4.93 |
| White | 111895 |
| Black | 41833 |
| Asian | 2627 |
| Native | 529 |
| Hispanic/Latino | 15643 |
| Bachelor's or higher | 46638 |

## Districts

- [GA-14](/us/states/ga/districts/14.md) — 100% (congressional)
- [GA Senate District 31](/us/states/ga/districts/senate/31.md) — 85% (state senate)
- [GA Senate District 30](/us/states/ga/districts/senate/30.md) — 15% (state senate)
- [GA House District 17](/us/states/ga/districts/house/17.md) — 36% (state house)
- [GA House District 16](/us/states/ga/districts/house/16.md) — 22% (state house)
- [GA House District 19](/us/states/ga/districts/house/19.md) — 15% (state house)
- [GA House District 18](/us/states/ga/districts/house/18.md) — 14% (state house)
- [GA House District 40](/us/states/ga/districts/house/40.md) — 13% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
