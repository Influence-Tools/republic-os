---
type: Jurisdiction
title: "Pike County, MS"
classification: county
fips: "28113"
state: "MS"
demographics:
  population: 39602
  population_under_18: 10100
  population_18_64: 22402
  population_65_plus: 7100
  median_household_income: 43814
  poverty_rate: 27.13
  homeownership_rate: 66.79
  unemployment_rate: 5.81
  median_home_value: 110800
  gini_index: 0.4953
  vacancy_rate: 21.84
  race_white: 16496
  race_black: 21253
  race_asian: 187
  race_native: 215
  hispanic: 667
  bachelors_plus: 5461
districts:
  - to: "us/states/ms/districts/03"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/ms/districts/senate/38"
    rel: in-district
    area_weight: 0.6217
  - to: "us/states/ms/districts/senate/39"
    rel: in-district
    area_weight: 0.3783
  - to: "us/states/ms/districts/house/98"
    rel: in-district
    area_weight: 0.4981
  - to: "us/states/ms/districts/house/96"
    rel: in-district
    area_weight: 0.202
  - to: "us/states/ms/districts/house/97"
    rel: in-district
    area_weight: 0.1781
  - to: "us/states/ms/districts/house/53"
    rel: in-district
    area_weight: 0.1218
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, ms]
timestamp: "2026-07-03"
---

# Pike County, MS

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 39602 |
| Under 18 | 10100 |
| 18–64 | 22402 |
| 65+ | 7100 |
| Median household income | 43814 |
| Poverty rate | 27.13 |
| Homeownership rate | 66.79 |
| Unemployment rate | 5.81 |
| Median home value | 110800 |
| Gini index | 0.4953 |
| Vacancy rate | 21.84 |
| White | 16496 |
| Black | 21253 |
| Asian | 187 |
| Native | 215 |
| Hispanic/Latino | 667 |
| Bachelor's or higher | 5461 |

## Districts

- [MS-03](/us/states/ms/districts/03.md) — 100% (congressional)
- [MS Senate District 38](/us/states/ms/districts/senate/38.md) — 62% (state senate)
- [MS Senate District 39](/us/states/ms/districts/senate/39.md) — 38% (state senate)
- [MS House District 98](/us/states/ms/districts/house/98.md) — 50% (state house)
- [MS House District 96](/us/states/ms/districts/house/96.md) — 20% (state house)
- [MS House District 97](/us/states/ms/districts/house/97.md) — 18% (state house)
- [MS House District 53](/us/states/ms/districts/house/53.md) — 12% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
