---
type: Jurisdiction
title: "Graham County, KS"
classification: county
fips: "20065"
state: "KS"
demographics:
  population: 2389
  population_under_18: 496
  population_18_64: 1247
  population_65_plus: 646
  median_household_income: 50650
  poverty_rate: 14.83
  homeownership_rate: 78.84
  unemployment_rate: 5.02
  median_home_value: 89900
  gini_index: 0.4248
  vacancy_rate: 15.83
  race_white: 2167
  race_black: 109
  race_asian: 16
  race_native: 0
  hispanic: 94
  bachelors_plus: 618
districts:
  - to: "us/states/ks/districts/01"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/ks/districts/senate/40"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ks/districts/house/110"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ks]
timestamp: "2026-07-03"
---

# Graham County, KS

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 2389 |
| Under 18 | 496 |
| 18–64 | 1247 |
| 65+ | 646 |
| Median household income | 50650 |
| Poverty rate | 14.83 |
| Homeownership rate | 78.84 |
| Unemployment rate | 5.02 |
| Median home value | 89900 |
| Gini index | 0.4248 |
| Vacancy rate | 15.83 |
| White | 2167 |
| Black | 109 |
| Asian | 16 |
| Native | 0 |
| Hispanic/Latino | 94 |
| Bachelor's or higher | 618 |

## Districts

- [KS-01](/us/states/ks/districts/01.md) — 100% (congressional)
- [KS Senate District 40](/us/states/ks/districts/senate/40.md) — 100% (state senate)
- [KS House District 110](/us/states/ks/districts/house/110.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
