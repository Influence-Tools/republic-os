---
type: Jurisdiction
title: "Bay County, MI"
classification: county
fips: "26017"
state: "MI"
demographics:
  population: 103008
  population_under_18: 20150
  population_18_64: 60290
  population_65_plus: 22568
  median_household_income: 61763
  poverty_rate: 13.25
  homeownership_rate: 77.03
  unemployment_rate: 4.34
  median_home_value: 152200
  gini_index: 0.4342
  vacancy_rate: 7.31
  race_white: 93440
  race_black: 1234
  race_asian: 525
  race_native: 230
  hispanic: 6117
  bachelors_plus: 21960
districts:
  - to: "us/states/mi/districts/08"
    rel: in-district
    area_weight: 0.7115
  - to: "us/states/mi/districts/senate/35"
    rel: in-district
    area_weight: 0.4281
  - to: "us/states/mi/districts/senate/34"
    rel: in-district
    area_weight: 0.1704
  - to: "us/states/mi/districts/senate/36"
    rel: in-district
    area_weight: 0.1122
  - to: "us/states/mi/districts/house/96"
    rel: in-district
    area_weight: 0.4815
  - to: "us/states/mi/districts/house/99"
    rel: in-district
    area_weight: 0.1736
  - to: "us/states/mi/districts/house/97"
    rel: in-district
    area_weight: 0.0552
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, mi]
timestamp: "2026-07-03"
---

# Bay County, MI

County jurisdiction — 1 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 103008 |
| Under 18 | 20150 |
| 18–64 | 60290 |
| 65+ | 22568 |
| Median household income | 61763 |
| Poverty rate | 13.25 |
| Homeownership rate | 77.03 |
| Unemployment rate | 4.34 |
| Median home value | 152200 |
| Gini index | 0.4342 |
| Vacancy rate | 7.31 |
| White | 93440 |
| Black | 1234 |
| Asian | 525 |
| Native | 230 |
| Hispanic/Latino | 6117 |
| Bachelor's or higher | 21960 |

## Districts

- [MI-08](/us/states/mi/districts/08.md) — 71% (congressional)
- [MI Senate District 35](/us/states/mi/districts/senate/35.md) — 43% (state senate)
- [MI Senate District 34](/us/states/mi/districts/senate/34.md) — 17% (state senate)
- [MI Senate District 36](/us/states/mi/districts/senate/36.md) — 11% (state senate)
- [MI House District 96](/us/states/mi/districts/house/96.md) — 48% (state house)
- [MI House District 99](/us/states/mi/districts/house/99.md) — 17% (state house)
- [MI House District 97](/us/states/mi/districts/house/97.md) — 6% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
