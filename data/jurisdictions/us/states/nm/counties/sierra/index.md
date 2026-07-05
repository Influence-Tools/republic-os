---
type: Jurisdiction
title: "Sierra County, NM"
classification: county
fips: "35051"
state: "NM"
demographics:
  population: 11500
  population_under_18: 1795
  population_18_64: 5240
  population_65_plus: 4465
  median_household_income: 41600
  poverty_rate: 21.38
  homeownership_rate: 71.8
  unemployment_rate: 4.16
  median_home_value: 152600
  gini_index: 0.4233
  vacancy_rate: 33.66
  race_white: 7971
  race_black: 25
  race_asian: 18
  race_native: 87
  hispanic: 3431
  bachelors_plus: 2155
districts:
  - to: "us/states/nm/districts/02"
    rel: in-district
    area_weight: 1.0
  - to: "us/states/nm/districts/senate/35"
    rel: in-district
    area_weight: 0.9998
  - to: "us/states/nm/districts/house/38"
    rel: in-district
    area_weight: 0.5307
  - to: "us/states/nm/districts/house/49"
    rel: in-district
    area_weight: 0.4692
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# Sierra County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 11500 |
| Under 18 | 1795 |
| 18–64 | 5240 |
| 65+ | 4465 |
| Median household income | 41600 |
| Poverty rate | 21.38 |
| Homeownership rate | 71.8 |
| Unemployment rate | 4.16 |
| Median home value | 152600 |
| Gini index | 0.4233 |
| Vacancy rate | 33.66 |
| White | 7971 |
| Black | 25 |
| Asian | 18 |
| Native | 87 |
| Hispanic/Latino | 3431 |
| Bachelor's or higher | 2155 |

## Districts

- [NM-02](/us/states/nm/districts/02.md) — 100% (congressional)
- [NM Senate District 35](/us/states/nm/districts/senate/35.md) — 100% (state senate)
- [NM House District 38](/us/states/nm/districts/house/38.md) — 53% (state house)
- [NM House District 49](/us/states/nm/districts/house/49.md) — 47% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
