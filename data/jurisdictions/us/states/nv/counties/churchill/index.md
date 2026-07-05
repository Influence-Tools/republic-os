---
type: Jurisdiction
title: "Churchill County, NV"
classification: county
fips: "32001"
state: "NV"
demographics:
  population: 25805
  population_under_18: 5863
  population_18_64: 14737
  population_65_plus: 5205
  median_household_income: 79163
  poverty_rate: 8.14
  homeownership_rate: 69.88
  unemployment_rate: 5.32
  median_home_value: 329900
  gini_index: 0.4168
  vacancy_rate: 13.55
  race_white: 19150
  race_black: 654
  race_asian: 608
  race_native: 925
  hispanic: 3928
  bachelors_plus: 3996
districts:
  - to: "us/states/nv/districts/02"
    rel: in-district
    area_weight: 0.9863
  - to: "us/states/nv/districts/04"
    rel: in-district
    area_weight: 0.0137
  - to: "us/states/nv/districts/senate/17"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nv/districts/house/38"
    rel: in-district
    area_weight: 0.9999
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nv]
timestamp: "2026-07-03"
---

# Churchill County, NV

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 25805 |
| Under 18 | 5863 |
| 18–64 | 14737 |
| 65+ | 5205 |
| Median household income | 79163 |
| Poverty rate | 8.14 |
| Homeownership rate | 69.88 |
| Unemployment rate | 5.32 |
| Median home value | 329900 |
| Gini index | 0.4168 |
| Vacancy rate | 13.55 |
| White | 19150 |
| Black | 654 |
| Asian | 608 |
| Native | 925 |
| Hispanic/Latino | 3928 |
| Bachelor's or higher | 3996 |

## Districts

- [NV-02](/us/states/nv/districts/02.md) — 99% (congressional)
- [NV-04](/us/states/nv/districts/04.md) — 1% (congressional)
- [NV Senate District 17](/us/states/nv/districts/senate/17.md) — 100% (state senate)
- [NV House District 38](/us/states/nv/districts/house/38.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
