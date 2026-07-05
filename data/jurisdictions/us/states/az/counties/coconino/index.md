---
type: Jurisdiction
title: "Coconino County, AZ"
classification: county
fips: "04005"
state: "AZ"
demographics:
  population: 145161
  population_under_18: 37438
  population_18_64: 54721
  population_65_plus: 53002
  median_household_income: 75164
  poverty_rate: 14.99
  homeownership_rate: 62.84
  unemployment_rate: 3.02
  median_home_value: 468600
  gini_index: 0.4934
  vacancy_rate: 18.0
  race_white: 84151
  race_black: 1612
  race_asian: 2920
  race_native: 37412
  hispanic: 23080
  bachelors_plus: 54535
districts:
  - to: "us/states/az/districts/02"
    rel: in-district
    area_weight: 0.9997
  - to: "us/states/az/districts/senate/6"
    rel: in-district
    area_weight: 0.8118
  - to: "us/states/az/districts/senate/7"
    rel: in-district
    area_weight: 0.1878
  - to: "us/states/az/districts/house/6"
    rel: in-district
    area_weight: 0.8118
  - to: "us/states/az/districts/house/7"
    rel: in-district
    area_weight: 0.1878
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, az]
timestamp: "2026-07-03"
---

# Coconino County, AZ

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 145161 |
| Under 18 | 37438 |
| 18–64 | 54721 |
| 65+ | 53002 |
| Median household income | 75164 |
| Poverty rate | 14.99 |
| Homeownership rate | 62.84 |
| Unemployment rate | 3.02 |
| Median home value | 468600 |
| Gini index | 0.4934 |
| Vacancy rate | 18.0 |
| White | 84151 |
| Black | 1612 |
| Asian | 2920 |
| Native | 37412 |
| Hispanic/Latino | 23080 |
| Bachelor's or higher | 54535 |

## Districts

- [AZ-02](/us/states/az/districts/02.md) — 100% (congressional)
- [AZ Senate District 6](/us/states/az/districts/senate/6.md) — 81% (state senate)
- [AZ Senate District 7](/us/states/az/districts/senate/7.md) — 19% (state senate)
- [AZ House District 6](/us/states/az/districts/house/6.md) — 81% (state house)
- [AZ House District 7](/us/states/az/districts/house/7.md) — 19% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
