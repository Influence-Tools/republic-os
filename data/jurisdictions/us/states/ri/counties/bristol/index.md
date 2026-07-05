---
type: Jurisdiction
title: "Bristol County, RI"
classification: county
fips: "44001"
state: "RI"
demographics:
  population: 50490
  population_under_18: 8973
  population_18_64: 30843
  population_65_plus: 10674
  median_household_income: 114490
  poverty_rate: 6.53
  homeownership_rate: 71.82
  unemployment_rate: 3.05
  median_home_value: 513800
  gini_index: 0.4592
  vacancy_rate: 6.99
  race_white: 45210
  race_black: 572
  race_asian: 1308
  race_native: 20
  hispanic: 2108
  bachelors_plus: 27880
districts:
  - to: "us/states/ri/districts/01"
    rel: in-district
    area_weight: 0.6737
  - to: "us/states/ri/districts/senate/32"
    rel: in-district
    area_weight: 0.3184
  - to: "us/states/ri/districts/senate/10"
    rel: in-district
    area_weight: 0.2355
  - to: "us/states/ri/districts/senate/11"
    rel: in-district
    area_weight: 0.0785
  - to: "us/states/ri/districts/house/67"
    rel: in-district
    area_weight: 0.2518
  - to: "us/states/ri/districts/house/68"
    rel: in-district
    area_weight: 0.155
  - to: "us/states/ri/districts/house/69"
    rel: in-district
    area_weight: 0.1167
  - to: "us/states/ri/districts/house/66"
    rel: in-district
    area_weight: 0.109
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ri]
timestamp: "2026-07-03"
---

# Bristol County, RI

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 50490 |
| Under 18 | 8973 |
| 18–64 | 30843 |
| 65+ | 10674 |
| Median household income | 114490 |
| Poverty rate | 6.53 |
| Homeownership rate | 71.82 |
| Unemployment rate | 3.05 |
| Median home value | 513800 |
| Gini index | 0.4592 |
| Vacancy rate | 6.99 |
| White | 45210 |
| Black | 572 |
| Asian | 1308 |
| Native | 20 |
| Hispanic/Latino | 2108 |
| Bachelor's or higher | 27880 |

## Districts

- [RI-01](/us/states/ri/districts/01.md) — 67% (congressional)
- [RI Senate District 32](/us/states/ri/districts/senate/32.md) — 32% (state senate)
- [RI Senate District 10](/us/states/ri/districts/senate/10.md) — 24% (state senate)
- [RI Senate District 11](/us/states/ri/districts/senate/11.md) — 8% (state senate)
- [RI House District 67](/us/states/ri/districts/house/67.md) — 25% (state house)
- [RI House District 68](/us/states/ri/districts/house/68.md) — 16% (state house)
- [RI House District 69](/us/states/ri/districts/house/69.md) — 12% (state house)
- [RI House District 66](/us/states/ri/districts/house/66.md) — 11% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
