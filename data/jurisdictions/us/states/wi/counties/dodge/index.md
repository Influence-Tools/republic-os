---
type: Jurisdiction
title: "Dodge County, WI"
classification: county
fips: "55027"
state: "WI"
demographics:
  population: 88742
  population_under_18: 17235
  population_18_64: 54648
  population_65_plus: 16859
  median_household_income: 75929
  poverty_rate: 8.5
  homeownership_rate: 71.32
  unemployment_rate: 3.78
  median_home_value: 231900
  gini_index: 0.3918
  vacancy_rate: 6.79
  race_white: 78439
  race_black: 2268
  race_asian: 554
  race_native: 524
  hispanic: 5941
  bachelors_plus: 16931
districts:
  - to: "us/states/wi/districts/05"
    rel: in-district
    area_weight: 0.6255
  - to: "us/states/wi/districts/06"
    rel: in-district
    area_weight: 0.3745
  - to: "us/states/wi/districts/senate/13"
    rel: in-district
    area_weight: 0.7626
  - to: "us/states/wi/districts/senate/33"
    rel: in-district
    area_weight: 0.1185
  - to: "us/states/wi/districts/senate/16"
    rel: in-district
    area_weight: 0.0786
  - to: "us/states/wi/districts/senate/20"
    rel: in-district
    area_weight: 0.0402
  - to: "us/states/wi/districts/house/37"
    rel: in-district
    area_weight: 0.435
  - to: "us/states/wi/districts/house/38"
    rel: in-district
    area_weight: 0.3277
  - to: "us/states/wi/districts/house/99"
    rel: in-district
    area_weight: 0.1185
  - to: "us/states/wi/districts/house/48"
    rel: in-district
    area_weight: 0.0785
  - to: "us/states/wi/districts/house/59"
    rel: in-district
    area_weight: 0.0402
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Dodge County, WI

County jurisdiction — 2 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 88742 |
| Under 18 | 17235 |
| 18–64 | 54648 |
| 65+ | 16859 |
| Median household income | 75929 |
| Poverty rate | 8.5 |
| Homeownership rate | 71.32 |
| Unemployment rate | 3.78 |
| Median home value | 231900 |
| Gini index | 0.3918 |
| Vacancy rate | 6.79 |
| White | 78439 |
| Black | 2268 |
| Asian | 554 |
| Native | 524 |
| Hispanic/Latino | 5941 |
| Bachelor's or higher | 16931 |

## Districts

- [WI-05](/us/states/wi/districts/05.md) — 63% (congressional)
- [WI-06](/us/states/wi/districts/06.md) — 37% (congressional)
- [WI Senate District 13](/us/states/wi/districts/senate/13.md) — 76% (state senate)
- [WI Senate District 33](/us/states/wi/districts/senate/33.md) — 12% (state senate)
- [WI Senate District 16](/us/states/wi/districts/senate/16.md) — 8% (state senate)
- [WI Senate District 20](/us/states/wi/districts/senate/20.md) — 4% (state senate)
- [WI House District 37](/us/states/wi/districts/house/37.md) — 44% (state house)
- [WI House District 38](/us/states/wi/districts/house/38.md) — 33% (state house)
- [WI House District 99](/us/states/wi/districts/house/99.md) — 12% (state house)
- [WI House District 48](/us/states/wi/districts/house/48.md) — 8% (state house)
- [WI House District 59](/us/states/wi/districts/house/59.md) — 4% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
