---
type: Jurisdiction
title: "Nueces County, TX"
classification: county
fips: "48355"
state: "TX"
demographics:
  population: 352955
  population_under_18: 83585
  population_18_64: 212594
  population_65_plus: 56776
  median_household_income: 66897
  poverty_rate: 17.4
  homeownership_rate: 59.68
  unemployment_rate: 5.16
  median_home_value: 208800
  gini_index: 0.4682
  vacancy_rate: 15.06
  race_white: 161750
  race_black: 13625
  race_asian: 8171
  race_native: 1665
  hispanic: 220501
  bachelors_plus: 75152
districts:
  - to: "us/states/tx/districts/27"
    rel: in-district
    area_weight: 0.7498
  - to: "us/states/tx/districts/senate/27"
    rel: in-district
    area_weight: 0.4761
  - to: "us/states/tx/districts/senate/20"
    rel: in-district
    area_weight: 0.2714
  - to: "us/states/tx/districts/house/34"
    rel: in-district
    area_weight: 0.5365
  - to: "us/states/tx/districts/house/32"
    rel: in-district
    area_weight: 0.2106
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, tx]
timestamp: "2026-07-03"
---

# Nueces County, TX

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 352955 |
| Under 18 | 83585 |
| 18–64 | 212594 |
| 65+ | 56776 |
| Median household income | 66897 |
| Poverty rate | 17.4 |
| Homeownership rate | 59.68 |
| Unemployment rate | 5.16 |
| Median home value | 208800 |
| Gini index | 0.4682 |
| Vacancy rate | 15.06 |
| White | 161750 |
| Black | 13625 |
| Asian | 8171 |
| Native | 1665 |
| Hispanic/Latino | 220501 |
| Bachelor's or higher | 75152 |

## Districts

- [TX-27](/us/states/tx/districts/27.md) — 75% (congressional)
- [TX Senate District 27](/us/states/tx/districts/senate/27.md) — 48% (state senate)
- [TX Senate District 20](/us/states/tx/districts/senate/20.md) — 27% (state senate)
- [TX House District 34](/us/states/tx/districts/house/34.md) — 54% (state house)
- [TX House District 32](/us/states/tx/districts/house/32.md) — 21% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
