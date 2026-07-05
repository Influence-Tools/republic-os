---
type: Jurisdiction
title: "Montgomery County, OH"
classification: county
fips: "39113"
state: "OH"
demographics:
  population: 536096
  population_under_18: 118834
  population_18_64: 317651
  population_65_plus: 99611
  median_household_income: 66139
  poverty_rate: 15.01
  homeownership_rate: 62.46
  unemployment_rate: 5.72
  median_home_value: 180900
  gini_index: 0.4587
  vacancy_rate: 8.51
  race_white: 366623
  race_black: 109607
  race_asian: 12151
  race_native: 485
  hispanic: 22744
  bachelors_plus: 162856
districts:
  - to: "us/states/oh/districts/10"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/oh/districts/senate/5"
    rel: in-district
    area_weight: 0.5538
  - to: "us/states/oh/districts/senate/6"
    rel: in-district
    area_weight: 0.4461
  - to: "us/states/oh/districts/house/40"
    rel: in-district
    area_weight: 0.3775
  - to: "us/states/oh/districts/house/37"
    rel: in-district
    area_weight: 0.213
  - to: "us/states/oh/districts/house/39"
    rel: in-district
    area_weight: 0.1763
  - to: "us/states/oh/districts/house/38"
    rel: in-district
    area_weight: 0.1426
  - to: "us/states/oh/districts/house/36"
    rel: in-district
    area_weight: 0.0906
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, oh]
timestamp: "2026-07-03"
---

# Montgomery County, OH

County jurisdiction — 10 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 536096 |
| Under 18 | 118834 |
| 18–64 | 317651 |
| 65+ | 99611 |
| Median household income | 66139 |
| Poverty rate | 15.01 |
| Homeownership rate | 62.46 |
| Unemployment rate | 5.72 |
| Median home value | 180900 |
| Gini index | 0.4587 |
| Vacancy rate | 8.51 |
| White | 366623 |
| Black | 109607 |
| Asian | 12151 |
| Native | 485 |
| Hispanic/Latino | 22744 |
| Bachelor's or higher | 162856 |

## Districts

- [OH-10](/us/states/oh/districts/10.md) — 100% (congressional)
- [OH Senate District 5](/us/states/oh/districts/senate/5.md) — 55% (state senate)
- [OH Senate District 6](/us/states/oh/districts/senate/6.md) — 45% (state senate)
- [OH House District 40](/us/states/oh/districts/house/40.md) — 38% (state house)
- [OH House District 37](/us/states/oh/districts/house/37.md) — 21% (state house)
- [OH House District 39](/us/states/oh/districts/house/39.md) — 18% (state house)
- [OH House District 38](/us/states/oh/districts/house/38.md) — 14% (state house)
- [OH House District 36](/us/states/oh/districts/house/36.md) — 9% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
