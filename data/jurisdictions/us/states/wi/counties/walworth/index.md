---
type: Jurisdiction
title: "Walworth County, WI"
classification: county
fips: "55127"
state: "WI"
demographics:
  population: 105657
  population_under_18: 20610
  population_18_64: 63952
  population_65_plus: 21095
  median_household_income: 80520
  poverty_rate: 9.36
  homeownership_rate: 70.63
  unemployment_rate: 2.88
  median_home_value: 302700
  gini_index: 0.452
  vacancy_rate: 20.39
  race_white: 90011
  race_black: 853
  race_asian: 916
  race_native: 392
  hispanic: 12821
  bachelors_plus: 31136
districts:
  - to: "us/states/wi/districts/01"
    rel: in-district
    area_weight: 0.9376
  - to: "us/states/wi/districts/05"
    rel: in-district
    area_weight: 0.0623
  - to: "us/states/wi/districts/senate/11"
    rel: in-district
    area_weight: 0.8719
  - to: "us/states/wi/districts/senate/15"
    rel: in-district
    area_weight: 0.1247
  - to: "us/states/wi/districts/house/31"
    rel: in-district
    area_weight: 0.5362
  - to: "us/states/wi/districts/house/33"
    rel: in-district
    area_weight: 0.2735
  - to: "us/states/wi/districts/house/43"
    rel: in-district
    area_weight: 0.1247
  - to: "us/states/wi/districts/house/32"
    rel: in-district
    area_weight: 0.0623
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Walworth County, WI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 105657 |
| Under 18 | 20610 |
| 18–64 | 63952 |
| 65+ | 21095 |
| Median household income | 80520 |
| Poverty rate | 9.36 |
| Homeownership rate | 70.63 |
| Unemployment rate | 2.88 |
| Median home value | 302700 |
| Gini index | 0.452 |
| Vacancy rate | 20.39 |
| White | 90011 |
| Black | 853 |
| Asian | 916 |
| Native | 392 |
| Hispanic/Latino | 12821 |
| Bachelor's or higher | 31136 |

## Districts

- [WI-01](/us/states/wi/districts/01.md) — 94% (congressional)
- [WI-05](/us/states/wi/districts/05.md) — 6% (congressional)
- [WI Senate District 11](/us/states/wi/districts/senate/11.md) — 87% (state senate)
- [WI Senate District 15](/us/states/wi/districts/senate/15.md) — 12% (state senate)
- [WI House District 31](/us/states/wi/districts/house/31.md) — 54% (state house)
- [WI House District 33](/us/states/wi/districts/house/33.md) — 27% (state house)
- [WI House District 43](/us/states/wi/districts/house/43.md) — 12% (state house)
- [WI House District 32](/us/states/wi/districts/house/32.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
