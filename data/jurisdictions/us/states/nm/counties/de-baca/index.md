---
type: Jurisdiction
title: "De Baca County, NM"
classification: county
fips: "35011"
state: "NM"
demographics:
  population: 1576
  population_under_18: 302
  population_18_64: 855
  population_65_plus: 419
  poverty_rate: 15.49
  homeownership_rate: 71.46
  unemployment_rate: 8.44
  median_home_value: 187500
  gini_index: 0.4285
  vacancy_rate: 34.92
  race_white: 672
  race_black: 1
  race_asian: 0
  race_native: 0
  hispanic: 1003
  bachelors_plus: 172
districts:
  - to: "us/states/nm/districts/01"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nm/districts/senate/27"
    rel: in-district
    area_weight: 0.9999
  - to: "us/states/nm/districts/house/63"
    rel: in-district
    area_weight: 0.9998
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, nm]
timestamp: "2026-07-03"
---

# De Baca County, NM

County jurisdiction.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 1576 |
| Under 18 | 302 |
| 18–64 | 855 |
| 65+ | 419 |
| Poverty rate | 15.49 |
| Homeownership rate | 71.46 |
| Unemployment rate | 8.44 |
| Median home value | 187500 |
| Gini index | 0.4285 |
| Vacancy rate | 34.92 |
| White | 672 |
| Black | 1 |
| Asian | 0 |
| Native | 0 |
| Hispanic/Latino | 1003 |
| Bachelor's or higher | 172 |

## Districts

- [NM-01](/us/states/nm/districts/01.md) — 100% (congressional)
- [NM Senate District 27](/us/states/nm/districts/senate/27.md) — 100% (state senate)
- [NM House District 63](/us/states/nm/districts/house/63.md) — 100% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
