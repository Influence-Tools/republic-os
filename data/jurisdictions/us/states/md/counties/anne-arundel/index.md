---
type: Jurisdiction
title: "Anne Arundel County, MD"
classification: county
fips: "24003"
state: "MD"
demographics:
  population: 598166
  population_under_18: 133881
  population_18_64: 369399
  population_65_plus: 94886
  median_household_income: 124911
  poverty_rate: 5.64
  homeownership_rate: 75.13
  unemployment_rate: 3.72
  median_home_value: 467900
  gini_index: 0.4179
  vacancy_rate: 4.87
  race_white: 379136
  race_black: 107044
  race_asian: 25238
  race_native: 3261
  hispanic: 62581
  bachelors_plus: 275283
districts:
  - to: "us/states/md/districts/03"
    rel: in-district
    area_weight: 0.4033
  - to: "us/states/md/districts/05"
    rel: in-district
    area_weight: 0.369
  - to: "us/states/md/districts/senate/30"
    rel: in-district
    area_weight: 0.2636
  - to: "us/states/md/districts/senate/33"
    rel: in-district
    area_weight: 0.1924
  - to: "us/states/md/districts/senate/31"
    rel: in-district
    area_weight: 0.1372
  - to: "us/states/md/districts/senate/32"
    rel: in-district
    area_weight: 0.0919
  - to: "us/states/md/districts/senate/21"
    rel: in-district
    area_weight: 0.0518
  - to: "us/states/md/districts/senate/12"
    rel: in-district
    area_weight: 0.0276
  - to: "us/states/md/districts/house/30b"
    rel: in-district
    area_weight: 0.192
  - to: "us/states/md/districts/house/31"
    rel: in-district
    area_weight: 0.1372
  - to: "us/states/md/districts/house/33b"
    rel: in-district
    area_weight: 0.127
  - to: "us/states/md/districts/house/32"
    rel: in-district
    area_weight: 0.0919
  - to: "us/states/md/districts/house/30a"
    rel: in-district
    area_weight: 0.0716
  - to: "us/states/md/districts/house/21"
    rel: in-district
    area_weight: 0.0518
  - to: "us/states/md/districts/house/33c"
    rel: in-district
    area_weight: 0.0438
  - to: "us/states/md/districts/house/12b"
    rel: in-district
    area_weight: 0.0276
  - to: "us/states/md/districts/house/33a"
    rel: in-district
    area_weight: 0.0216
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, md]
timestamp: "2026-07-03"
---

# Anne Arundel County, MD

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 598166 |
| Under 18 | 133881 |
| 18–64 | 369399 |
| 65+ | 94886 |
| Median household income | 124911 |
| Poverty rate | 5.64 |
| Homeownership rate | 75.13 |
| Unemployment rate | 3.72 |
| Median home value | 467900 |
| Gini index | 0.4179 |
| Vacancy rate | 4.87 |
| White | 379136 |
| Black | 107044 |
| Asian | 25238 |
| Native | 3261 |
| Hispanic/Latino | 62581 |
| Bachelor's or higher | 275283 |

## Districts

- [MD-03](/us/states/md/districts/03.md) — 40% (congressional)
- [MD-05](/us/states/md/districts/05.md) — 37% (congressional)
- [MD Senate District 30](/us/states/md/districts/senate/30.md) — 26% (state senate)
- [MD Senate District 33](/us/states/md/districts/senate/33.md) — 19% (state senate)
- [MD Senate District 31](/us/states/md/districts/senate/31.md) — 14% (state senate)
- [MD Senate District 32](/us/states/md/districts/senate/32.md) — 9% (state senate)
- [MD Senate District 21](/us/states/md/districts/senate/21.md) — 5% (state senate)
- [MD Senate District 12](/us/states/md/districts/senate/12.md) — 3% (state senate)
- [MD House District 30B](/us/states/md/districts/house/30b.md) — 19% (state house)
- [MD House District 31](/us/states/md/districts/house/31.md) — 14% (state house)
- [MD House District 33B](/us/states/md/districts/house/33b.md) — 13% (state house)
- [MD House District 32](/us/states/md/districts/house/32.md) — 9% (state house)
- [MD House District 30A](/us/states/md/districts/house/30a.md) — 7% (state house)
- [MD House District 21](/us/states/md/districts/house/21.md) — 5% (state house)
- [MD House District 33C](/us/states/md/districts/house/33c.md) — 4% (state house)
- [MD House District 12B](/us/states/md/districts/house/12b.md) — 3% (state house)
- [MD House District 33A](/us/states/md/districts/house/33a.md) — 2% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
