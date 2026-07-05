---
type: Jurisdiction
title: "Racine County, WI"
classification: county
fips: "55101"
state: "WI"
demographics:
  population: 197532
  population_under_18: 44901
  population_18_64: 116829
  population_65_plus: 35802
  median_household_income: 78096
  poverty_rate: 10.31
  homeownership_rate: 71.04
  unemployment_rate: 4.41
  median_home_value: 251400
  gini_index: 0.4251
  vacancy_rate: 6.13
  race_white: 142655
  race_black: 20827
  race_asian: 2370
  race_native: 920
  hispanic: 29754
  bachelors_plus: 51594
districts:
  - to: "us/states/wi/districts/01"
    rel: in-district
    area_weight: 0.4293
  - to: "us/states/wi/districts/senate/11"
    rel: in-district
    area_weight: 0.1664
  - to: "us/states/wi/districts/senate/21"
    rel: in-district
    area_weight: 0.1195
  - to: "us/states/wi/districts/senate/28"
    rel: in-district
    area_weight: 0.0908
  - to: "us/states/wi/districts/senate/22"
    rel: in-district
    area_weight: 0.0528
  - to: "us/states/wi/districts/house/33"
    rel: in-district
    area_weight: 0.1664
  - to: "us/states/wi/districts/house/63"
    rel: in-district
    area_weight: 0.0956
  - to: "us/states/wi/districts/house/84"
    rel: in-district
    area_weight: 0.0908
  - to: "us/states/wi/districts/house/66"
    rel: in-district
    area_weight: 0.0528
  - to: "us/states/wi/districts/house/62"
    rel: in-district
    area_weight: 0.024
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Racine County, WI

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 197532 |
| Under 18 | 44901 |
| 18–64 | 116829 |
| 65+ | 35802 |
| Median household income | 78096 |
| Poverty rate | 10.31 |
| Homeownership rate | 71.04 |
| Unemployment rate | 4.41 |
| Median home value | 251400 |
| Gini index | 0.4251 |
| Vacancy rate | 6.13 |
| White | 142655 |
| Black | 20827 |
| Asian | 2370 |
| Native | 920 |
| Hispanic/Latino | 29754 |
| Bachelor's or higher | 51594 |

## Districts

- [WI-01](/us/states/wi/districts/01.md) — 43% (congressional)
- [WI Senate District 11](/us/states/wi/districts/senate/11.md) — 17% (state senate)
- [WI Senate District 21](/us/states/wi/districts/senate/21.md) — 12% (state senate)
- [WI Senate District 28](/us/states/wi/districts/senate/28.md) — 9% (state senate)
- [WI Senate District 22](/us/states/wi/districts/senate/22.md) — 5% (state senate)
- [WI House District 33](/us/states/wi/districts/house/33.md) — 17% (state house)
- [WI House District 63](/us/states/wi/districts/house/63.md) — 10% (state house)
- [WI House District 84](/us/states/wi/districts/house/84.md) — 9% (state house)
- [WI House District 66](/us/states/wi/districts/house/66.md) — 5% (state house)
- [WI House District 62](/us/states/wi/districts/house/62.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
