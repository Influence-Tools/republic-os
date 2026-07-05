---
type: Jurisdiction
title: "Lyon County, NV"
classification: county
fips: "32019"
state: "NV"
demographics:
  population: 61680
  population_under_18: 12423
  population_18_64: 35544
  population_65_plus: 13713
  median_household_income: 80812
  poverty_rate: 11.7
  homeownership_rate: 76.66
  unemployment_rate: 6.47
  median_home_value: 366100
  gini_index: 0.3979
  vacancy_rate: 6.65
  race_white: 45797
  race_black: 836
  race_asian: 804
  race_native: 1134
  hispanic: 12034
  bachelors_plus: 10123
districts:
  - to: "us/states/nv/districts/02"
    rel: in-district
    area_weight: 0.6372
  - to: "us/states/nv/districts/04"
    rel: in-district
    area_weight: 0.3628
  - to: "us/states/nv/districts/senate/17"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nv/districts/house/38"
    rel: in-district
    area_weight: 0.8342
  - to: "us/states/nv/districts/house/39"
    rel: in-district
    area_weight: 0.1657
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nv]
timestamp: "2026-07-03"
---

# Lyon County, NV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 61680 |
| Under 18 | 12423 |
| 18–64 | 35544 |
| 65+ | 13713 |
| Median household income | 80812 |
| Poverty rate | 11.7 |
| Homeownership rate | 76.66 |
| Unemployment rate | 6.47 |
| Median home value | 366100 |
| Gini index | 0.3979 |
| Vacancy rate | 6.65 |
| White | 45797 |
| Black | 836 |
| Asian | 804 |
| Native | 1134 |
| Hispanic/Latino | 12034 |
| Bachelor's or higher | 10123 |

## Districts

- [NV-02](/us/states/nv/districts/02.md) — 64% (congressional)
- [NV-04](/us/states/nv/districts/04.md) — 36% (congressional)
- [NV Senate District 17](/us/states/nv/districts/senate/17.md) — 100% (state senate)
- [NV House District 38](/us/states/nv/districts/house/38.md) — 83% (state house)
- [NV House District 39](/us/states/nv/districts/house/39.md) — 17% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
