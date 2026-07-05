---
type: Jurisdiction
title: "Winnebago County, WI"
classification: county
fips: "55139"
state: "WI"
demographics:
  population: 171769
  population_under_18: 34694
  population_18_64: 107181
  population_65_plus: 29894
  median_household_income: 74925
  poverty_rate: 11.33
  homeownership_rate: 65.77
  unemployment_rate: 2.18
  median_home_value: 225800
  gini_index: 0.4239
  vacancy_rate: 6.02
  race_white: 148625
  race_black: 4785
  race_asian: 5561
  race_native: 657
  hispanic: 8736
  bachelors_plus: 48220
districts:
  - to: "us/states/wi/districts/06"
    rel: in-district
    area_weight: 0.9199
  - to: "us/states/wi/districts/08"
    rel: in-district
    area_weight: 0.0801
  - to: "us/states/wi/districts/senate/19"
    rel: in-district
    area_weight: 0.6646
  - to: "us/states/wi/districts/senate/18"
    rel: in-district
    area_weight: 0.1168
  - to: "us/states/wi/districts/senate/13"
    rel: in-district
    area_weight: 0.0623
  - to: "us/states/wi/districts/house/55"
    rel: in-district
    area_weight: 0.5461
  - to: "us/states/wi/districts/house/57"
    rel: in-district
    area_weight: 0.1184
  - to: "us/states/wi/districts/house/54"
    rel: in-district
    area_weight: 0.0708
  - to: "us/states/wi/districts/house/39"
    rel: in-district
    area_weight: 0.0623
  - to: "us/states/wi/districts/house/53"
    rel: in-district
    area_weight: 0.046
sources:
  - field: demographics
    source: "Census ACS 2023"
  - field: districts
    source: "PostGIS area-intersection over Census TIGER 2024 boundaries"
confidence: official
tags: [jurisdiction, county, wi]
timestamp: "2026-07-03"
---

# Winnebago County, WI

County jurisdiction — 3 officeholders mapped.

## Demographics (ACS 2023)

| Measure | Value |
| --- | --- |
| Population | 171769 |
| Under 18 | 34694 |
| 18–64 | 107181 |
| 65+ | 29894 |
| Median household income | 74925 |
| Poverty rate | 11.33 |
| Homeownership rate | 65.77 |
| Unemployment rate | 2.18 |
| Median home value | 225800 |
| Gini index | 0.4239 |
| Vacancy rate | 6.02 |
| White | 148625 |
| Black | 4785 |
| Asian | 5561 |
| Native | 657 |
| Hispanic/Latino | 8736 |
| Bachelor's or higher | 48220 |

## Districts

- [WI-06](/us/states/wi/districts/06.md) — 92% (congressional)
- [WI-08](/us/states/wi/districts/08.md) — 8% (congressional)
- [WI Senate District 19](/us/states/wi/districts/senate/19.md) — 66% (state senate)
- [WI Senate District 18](/us/states/wi/districts/senate/18.md) — 12% (state senate)
- [WI Senate District 13](/us/states/wi/districts/senate/13.md) — 6% (state senate)
- [WI House District 55](/us/states/wi/districts/house/55.md) — 55% (state house)
- [WI House District 57](/us/states/wi/districts/house/57.md) — 12% (state house)
- [WI House District 54](/us/states/wi/districts/house/54.md) — 7% (state house)
- [WI House District 39](/us/states/wi/districts/house/39.md) — 6% (state house)
- [WI House District 53](/us/states/wi/districts/house/53.md) — 5% (state house)

## Source

- demographics: Census ACS 2023
- districts: PostGIS area-intersection over Census TIGER 2024 boundaries
