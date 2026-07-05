---
type: Jurisdiction
title: "Matanuska-Susitna Borough, AK"
classification: county
fips: "02170"
state: "AK"
demographics:
  population: 117613
  population_under_18: 32803
  population_18_64: 39763
  population_65_plus: 45047
  median_household_income: 96643
  poverty_rate: 9.0
  homeownership_rate: 80.05
  unemployment_rate: 4.79
  median_home_value: 379500
  gini_index: 0.4264
  vacancy_rate: 23.2
  race_white: 88929
  race_black: 1371
  race_asian: 1788
  race_native: 7674
  hispanic: 6817
  bachelors_plus: 28406
districts:
  - to: "us/states/ak/districts/00"
    rel: in-district
    area_weight: 0.9895
  - to: "us/states/ak/districts/senate/o"
    rel: in-district
    area_weight: 0.9744
  - to: "us/states/ak/districts/senate/m"
    rel: in-district
    area_weight: 0.0113
  - to: "us/states/ak/districts/house/30"
    rel: in-district
    area_weight: 0.4949
  - to: "us/states/ak/districts/house/29"
    rel: in-district
    area_weight: 0.4796
  - to: "us/states/ak/districts/house/25"
    rel: in-district
    area_weight: 0.0081
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ak]
timestamp: "2026-07-03"
---

# Matanuska-Susitna Borough, AK

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 117613 |
| Under 18 | 32803 |
| 18–64 | 39763 |
| 65+ | 45047 |
| Median household income | 96643 |
| Poverty rate | 9.0 |
| Homeownership rate | 80.05 |
| Unemployment rate | 4.79 |
| Median home value | 379500 |
| Gini index | 0.4264 |
| Vacancy rate | 23.2 |
| White | 88929 |
| Black | 1371 |
| Asian | 1788 |
| Native | 7674 |
| Hispanic/Latino | 6817 |
| Bachelor's or higher | 28406 |

## Districts

- [AK-00](/us/states/ak/districts/00.md) — 99% (congressional)
- [AK Senate District O](/us/states/ak/districts/senate/o.md) — 97% (state senate)
- [AK Senate District M](/us/states/ak/districts/senate/m.md) — 1% (state senate)
- [AK House District 30](/us/states/ak/districts/house/30.md) — 49% (state house)
- [AK House District 29](/us/states/ak/districts/house/29.md) — 48% (state house)
- [AK House District 25](/us/states/ak/districts/house/25.md) — 1% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
