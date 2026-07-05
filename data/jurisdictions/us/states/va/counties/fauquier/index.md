---
type: Jurisdiction
title: "Fauquier County, VA"
classification: county
fips: "51061"
state: "VA"
demographics:
  population: 74577
  population_under_18: 17358
  population_18_64: 44416
  population_65_plus: 12803
  median_household_income: 130189
  poverty_rate: 6.76
  homeownership_rate: 78.84
  unemployment_rate: 2.86
  median_home_value: 573700
  gini_index: 0.4159
  vacancy_rate: 6.64
  race_white: 59529
  race_black: 4688
  race_asian: 1308
  race_native: 156
  hispanic: 9257
  bachelors_plus: 29805
districts:
  - to: "us/states/va/districts/10"
    rel: in-district
    area_weight: 0.9962
  - to: "us/states/va/districts/senate/31"
    rel: in-district
    area_weight: 0.5609
  - to: "us/states/va/districts/senate/28"
    rel: in-district
    area_weight: 0.439
  - to: "us/states/va/districts/house/61"
    rel: in-district
    area_weight: 0.5689
  - to: "us/states/va/districts/house/30"
    rel: in-district
    area_weight: 0.4309
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, va]
timestamp: "2026-07-03"
---

# Fauquier County, VA

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 74577 |
| Under 18 | 17358 |
| 18–64 | 44416 |
| 65+ | 12803 |
| Median household income | 130189 |
| Poverty rate | 6.76 |
| Homeownership rate | 78.84 |
| Unemployment rate | 2.86 |
| Median home value | 573700 |
| Gini index | 0.4159 |
| Vacancy rate | 6.64 |
| White | 59529 |
| Black | 4688 |
| Asian | 1308 |
| Native | 156 |
| Hispanic/Latino | 9257 |
| Bachelor's or higher | 29805 |

## Districts

- [VA-10](/us/states/va/districts/10.md) — 100% (congressional)
- [VA Senate District 31](/us/states/va/districts/senate/31.md) — 56% (state senate)
- [VA Senate District 28](/us/states/va/districts/senate/28.md) — 44% (state senate)
- [VA House District 61](/us/states/va/districts/house/61.md) — 57% (state house)
- [VA House District 30](/us/states/va/districts/house/30.md) — 43% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
